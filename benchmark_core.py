#!/usr/bin/python3
"""Shared benchmark logic for CLI and GUI frontends."""

from __future__ import annotations

from dataclasses import dataclass
import multiprocessing as mp
import platform
import time
from typing import Callable, Dict, List, Optional, Tuple

import cpuinfo


@dataclass(frozen=True)
class BenchmarkConfig:
    iterations: int = 10_000
    repeats: int = 10


def get_system_info() -> Dict[str, str]:
    info = cpuinfo.get_cpu_info()
    return {
        "cpu": info.get("brand_raw", "Unknown"),
        "arch": info.get("arch_string_raw", "Unknown"),
        "os": f"{platform.system()} {platform.release()}",
        "python": platform.python_version(),
    }


def _workload() -> None:
    for x in range(1, 1000):
        3.141592 * 2**x
    for x in range(1, 10000):
        float(x) / 3.141592
    for x in range(1, 10000):
        float(3.141592) / x


def run_single_core(
    config: BenchmarkConfig,
    progress_cb: Optional[Callable[[int, int, float], None]] = None,
) -> Dict[str, object]:
    attempts: List[float] = []
    total_duration = 0.0

    for attempt in range(config.repeats):
        start = time.perf_counter()
        for _ in range(config.iterations):
            _workload()
        duration = round(time.perf_counter() - start, 3)
        attempts.append(duration)
        total_duration += duration
        if progress_cb:
            progress_cb(attempt + 1, config.repeats, duration)

    average_duration = round(total_duration / config.repeats, 3)
    ops_per_second = config.iterations / average_duration if average_duration else 0.0
    return {
        "attempts": attempts,
        "average_seconds": average_duration,
        "ops_per_second": ops_per_second,
    }


def _multicore_worker(chunk_size: int) -> Tuple[float, int]:
    start = time.perf_counter()
    for _ in range(chunk_size):
        _workload()
    duration = round(time.perf_counter() - start, 3)
    return duration, chunk_size


def _chunk_distribution(iterations: int, cores: int) -> List[int]:
    base = iterations // cores
    remainder = iterations % cores
    chunks = [base] * cores
    for idx in range(remainder):
        chunks[idx] += 1
    return chunks


def run_multi_core(
    config: BenchmarkConfig,
    progress_cb: Optional[Callable[[int, int, float], None]] = None,
) -> Dict[str, object]:
    num_cores = mp.cpu_count()
    chunks = _chunk_distribution(config.iterations, num_cores)
    tasks = [chunk for chunk in chunks if chunk > 0]

    if not tasks:
        return {
            "core_durations": [],
            "average_core_seconds": 0.0,
            "total_time": 0.0,
            "total_operations": 0,
            "ops_per_second": 0.0,
            "used_cores": 0,
        }

    total_ops = 0
    core_durations: List[float] = []
    start_time = time.perf_counter()
    ctx = mp.get_context("spawn")

    with ctx.Pool(processes=len(tasks)) as pool:
        for idx, (duration, ops) in enumerate(pool.imap_unordered(_multicore_worker, tasks), start=1):
            core_durations.append(duration)
            total_ops += ops
            if progress_cb:
                progress_cb(idx, len(tasks), duration)

    total_time = round(time.perf_counter() - start_time, 3)
    average_core_seconds = round(sum(core_durations) / len(core_durations), 3) if core_durations else 0.0
    ops_per_second = total_ops / total_time if total_time else 0.0

    return {
        "core_durations": core_durations,
        "average_core_seconds": average_core_seconds,
        "total_time": total_time,
        "total_operations": total_ops,
        "ops_per_second": ops_per_second,
        "used_cores": len(tasks),
    }


def run_full_benchmark(
    config: BenchmarkConfig,
    single_progress_cb: Optional[Callable[[int, int, float], None]] = None,
    multi_progress_cb: Optional[Callable[[int, int, float], None]] = None,
) -> Dict[str, object]:
    single = run_single_core(config, progress_cb=single_progress_cb)
    multi = run_multi_core(config, progress_cb=multi_progress_cb)
    single_ops = float(single["ops_per_second"])
    multi_ops = float(multi["ops_per_second"])
    speedup = multi_ops / single_ops if single_ops else 0.0
    return {
        "single": single,
        "multi": multi,
        "speedup": speedup,
    }
