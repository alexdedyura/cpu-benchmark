#!/usr/bin/python3
# Python CPU Benchmark by Alex Dedyura (Windows, macOS, Linux)

import multiprocessing as mp

from benchmark_core import BenchmarkConfig, get_system_info, run_multi_core, run_single_core


def main() -> None:
    info = get_system_info()
    print("Python CPU Benchmark by Alex Dedyura (Windows, macOS (Darwin), Linux)")
    print("CPU: " + info["cpu"])
    print("Arch: " + info["arch"])
    print("OS: " + info["os"])
    print("Python: " + info["python"])

    config = BenchmarkConfig(iterations=10_000, repeats=10)

    print("\n--- Single-Core Benchmark ---\n")

    def single_progress(attempt: int, total: int, seconds: float) -> None:
        print(f"Attempt {attempt}: {seconds}s")

    def multi_progress(core: int, total: int, seconds: float) -> None:
        print(f"Core {core}/{total} finished: {seconds}s")

    single = run_single_core(config, progress_cb=single_progress)
    print(f"\nPerfomance (avg, 1 core): {single['average_seconds']}s")
    print(f"Single-Core Operations per second: {int(single['ops_per_second'])}\n")
    print("\n--- Multicore Benchmark ---\n")
    print(f"Utilizing up to {min(mp.cpu_count(), config.iterations)} cores for benchmarking...\n")
    multi = run_multi_core(config, progress_cb=multi_progress)
    print(f"\nUsed cores: {multi['used_cores']}\n")
    print(f"Perfomance (avg, all cores): {multi['average_core_seconds']}s")
    print("\nMulticore Results:")
    print(f"Total wall time: {multi['total_time']}s")
    print(f"Total operations completed: {multi['total_operations']}")
    print(f"Multi-Core Operations per second: {int(multi['ops_per_second'])}")
    speedup = (
        float(multi["ops_per_second"]) / float(single["ops_per_second"])
        if float(single["ops_per_second"])
        else 0.0
    )
    print(f"\nSpeedup vs Single-Core: {speedup:.2f}x")


if __name__ == "__main__":
    mp.freeze_support()
    try:
        main()
    except KeyboardInterrupt:
        print("\nBenchmark interrupted. Exiting...")
        raise SystemExit(1)
