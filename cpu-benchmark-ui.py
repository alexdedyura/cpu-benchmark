#!/usr/bin/python3
"""Cross-platform Tkinter UI for CPU Benchmark."""

from __future__ import annotations

import multiprocessing as mp
import queue
import threading
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from typing import Optional

from benchmark_core import BenchmarkConfig, get_system_info, run_full_benchmark


BG = "#f3f6fb"
CARD_BG = "#ffffff"
TEXT = "#1f2a37"
MUTED = "#5b6472"
ACCENT = "#2f6fed"
ACCENT_SOFT = "#e8efff"
BORDER = "#d8e0ee"


class BenchmarkApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("CPU Benchmark")
        self.minsize(860, 620)
        self.geometry("1000x720")
        self.configure(bg=BG)

        self.info = get_system_info()
        self.worker_thread: Optional[threading.Thread] = None
        self.events: queue.Queue = queue.Queue()

        self.iterations_var = tk.StringVar(value="10000")
        self.repeats_var = tk.StringVar(value="10")
        self.status_var = tk.StringVar(value="Ready")
        self.single_perf_var = tk.StringVar(value="-")
        self.multi_perf_var = tk.StringVar(value="-")
        self.speedup_var = tk.StringVar(value="-")

        self._configure_style()
        self._build_ui()

    def _configure_style(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Root.TFrame", background=BG)
        style.configure("Card.TLabelframe", background=CARD_BG, bordercolor=BORDER, relief="solid")
        style.configure("Card.TLabelframe.Label", background=CARD_BG, foreground=TEXT, font=("Segoe UI", 10, "bold"))
        style.configure("Title.TLabel", background=BG, foreground=TEXT, font=("Segoe UI Semibold", 22))
        style.configure("Subtitle.TLabel", background=BG, foreground=MUTED, font=("Segoe UI", 10))
        style.configure("Info.TLabel", background=CARD_BG, foreground=TEXT, font=("Segoe UI", 10))
        style.configure("Muted.TLabel", background=BG, foreground=MUTED, font=("Segoe UI", 10))
        style.configure("MetricName.TLabel", background=CARD_BG, foreground=MUTED, font=("Segoe UI", 10))
        style.configure("MetricValue.TLabel", background=CARD_BG, foreground=TEXT, font=("Segoe UI Semibold", 18))
        style.configure("Run.TButton", font=("Segoe UI Semibold", 10), padding=(16, 8))
        style.map("Run.TButton", background=[("!disabled", ACCENT)], foreground=[("!disabled", "#ffffff")])
        style.configure(
            "Accent.Horizontal.TProgressbar",
            background=ACCENT,
            troughcolor=ACCENT_SOFT,
            bordercolor=ACCENT_SOFT,
            lightcolor=ACCENT,
            darkcolor=ACCENT,
        )

    def _build_ui(self) -> None:
        root = ttk.Frame(self, padding=16, style="Root.TFrame")
        root.pack(fill=tk.BOTH, expand=True)
        root.grid_columnconfigure(0, weight=1)

        header = ttk.Frame(root, style="Root.TFrame")
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="CPU Benchmark", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="Cross-platform benchmark runner for Windows, macOS and Linux",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(2, 0))

        top = ttk.Frame(root, style="Root.TFrame")
        top.grid(row=1, column=0, sticky="ew", pady=(14, 0))
        top.grid_columnconfigure(0, weight=3)
        top.grid_columnconfigure(1, weight=2)

        info_frame = ttk.LabelFrame(top, text="System Info", padding=12, style="Card.TLabelframe")
        info_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        info_frame.grid_columnconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)
        ttk.Label(info_frame, text=f"CPU: {self.info['cpu']}", style="Info.TLabel").grid(row=0, column=0, sticky="w", pady=2)
        ttk.Label(info_frame, text=f"Arch: {self.info['arch']}", style="Info.TLabel").grid(row=1, column=0, sticky="w", pady=2)
        ttk.Label(info_frame, text=f"OS: {self.info['os']}", style="Info.TLabel").grid(row=0, column=1, sticky="w", pady=2)
        ttk.Label(info_frame, text=f"Python: {self.info['python']}", style="Info.TLabel").grid(row=1, column=1, sticky="w", pady=2)

        controls = ttk.LabelFrame(top, text="Run Settings", padding=12, style="Card.TLabelframe")
        controls.grid(row=0, column=1, sticky="nsew")
        ttk.Label(controls, text="Iterations", style="Info.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 4))
        ttk.Entry(controls, textvariable=self.iterations_var, width=12).grid(row=1, column=0, sticky="w")
        ttk.Label(controls, text="Repeats", style="Info.TLabel").grid(row=2, column=0, sticky="w", pady=(10, 4))
        ttk.Entry(controls, textvariable=self.repeats_var, width=12).grid(row=3, column=0, sticky="w")
        self.start_btn = ttk.Button(controls, text="Start Benchmark", style="Run.TButton", command=self.start_benchmark)
        self.start_btn.grid(row=4, column=0, sticky="w", pady=(14, 0))

        self.progress = ttk.Progressbar(root, mode="indeterminate", style="Accent.Horizontal.TProgressbar")
        self.progress.grid(row=2, column=0, sticky="ew", pady=(12, 0))
        ttk.Label(root, textvariable=self.status_var, style="Muted.TLabel").grid(row=3, column=0, sticky="w", pady=(4, 0))

        metrics = ttk.Frame(root, style="Root.TFrame")
        metrics.grid(row=4, column=0, sticky="ew", pady=(12, 0))
        metrics.grid_columnconfigure(0, weight=1)
        metrics.grid_columnconfigure(1, weight=1)
        metrics.grid_columnconfigure(2, weight=1)

        self._metric_card(metrics, 0, "Perfomance (avg, 1 core)", self.single_perf_var)
        self._metric_card(metrics, 1, "Perfomance (avg, all cores)", self.multi_perf_var)
        self._metric_card(metrics, 2, "Speedup", self.speedup_var)

        log_frame = ttk.LabelFrame(root, text="Run Log", padding=10, style="Card.TLabelframe")
        log_frame.grid(row=5, column=0, sticky="nsew", pady=(12, 0))
        root.grid_rowconfigure(5, weight=1)

        self.log = ScrolledText(
            log_frame,
            wrap=tk.WORD,
            height=16,
            font=("Consolas", 10),
            bg="#fbfcff",
            fg=TEXT,
            bd=0,
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=ACCENT,
            insertbackground=TEXT,
        )
        self.log.pack(fill=tk.BOTH, expand=True)
        self.log.configure(state=tk.DISABLED)

    def _metric_card(self, parent: ttk.Frame, column: int, title: str, value_var: tk.StringVar) -> None:
        card = ttk.LabelFrame(parent, text="", padding=12, style="Card.TLabelframe")
        card.grid(row=0, column=column, sticky="nsew", padx=(0, 8) if column < 2 else 0)
        ttk.Label(card, text=title, style="MetricName.TLabel").pack(anchor="w")
        ttk.Label(card, textvariable=value_var, style="MetricValue.TLabel").pack(anchor="w", pady=(6, 0))

    def _append_log(self, text: str) -> None:
        self.log.configure(state=tk.NORMAL)
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)
        self.log.configure(state=tk.DISABLED)

    def _parse_positive_int(self, value: str, field: str) -> int:
        try:
            parsed = int(value.strip())
        except ValueError as exc:
            raise ValueError(f"{field} must be an integer.") from exc
        if parsed <= 0:
            raise ValueError(f"{field} must be greater than 0.")
        return parsed

    def start_benchmark(self) -> None:
        if self.worker_thread and self.worker_thread.is_alive():
            return

        try:
            iterations = self._parse_positive_int(self.iterations_var.get(), "Iterations")
            repeats = self._parse_positive_int(self.repeats_var.get(), "Repeats")
        except ValueError as exc:
            messagebox.showerror("Invalid input", str(exc))
            return

        self.start_btn.configure(state=tk.DISABLED)
        self.progress.start(10)
        self.status_var.set("Benchmark in progress...")
        self.single_perf_var.set("-")
        self.multi_perf_var.set("-")
        self.speedup_var.set("-")

        self.log.configure(state=tk.NORMAL)
        self.log.delete("1.0", tk.END)
        self.log.configure(state=tk.DISABLED)
        self._append_log("Starting benchmark...")
        self._append_log(f"CPU: {self.info['cpu']}")
        self._append_log(f"Config: iterations={iterations}, repeats={repeats}")

        config = BenchmarkConfig(iterations=iterations, repeats=repeats)
        self.worker_thread = threading.Thread(target=self._worker, args=(config,), daemon=True)
        self.worker_thread.start()
        self.after(100, self._poll_events)

    def _worker(self, config: BenchmarkConfig) -> None:
        def single_progress(attempt: int, total: int, seconds: float) -> None:
            self.events.put(("single_progress", attempt, total, seconds))

        def multi_progress(core: int, total: int, seconds: float) -> None:
            self.events.put(("multi_progress", core, total, seconds))

        try:
            result = run_full_benchmark(
                config,
                single_progress_cb=single_progress,
                multi_progress_cb=multi_progress,
            )
            self.events.put(("done", result))
        except Exception as exc:  # pylint: disable=broad-except
            self.events.put(("error", str(exc)))
        finally:
            self.events.put(("finished",))

    def _poll_events(self) -> None:
        while True:
            try:
                event = self.events.get_nowait()
            except queue.Empty:
                break

            kind = event[0]
            if kind == "single_progress":
                _, attempt, total, seconds = event
                self._append_log(f"[Single] Attempt {attempt}/{total}: {seconds:.3f}s")
            elif kind == "multi_progress":
                _, core, total, seconds = event
                self._append_log(f"[Multi] Worker {core}/{total} finished: {seconds:.3f}s")
            elif kind == "done":
                result = event[1]
                single = result["single"]
                multi = result["multi"]

                self.single_perf_var.set(f"{float(single['average_seconds']):.3f} s")
                self.multi_perf_var.set(f"{float(multi['average_core_seconds']):.3f} s")
                self.speedup_var.set(f"{float(result['speedup']):.2f}x")

                self._append_log("")
                self._append_log(f"Perfomance (avg, 1 core): {float(single['average_seconds']):.3f}s")
                self._append_log(f"Perfomance (avg, all cores): {float(multi['average_core_seconds']):.3f}s")
                self._append_log(f"Multi total wall time: {float(multi['total_time']):.3f}s")
                self._append_log(f"Speedup: {float(result['speedup']):.2f}x")
            elif kind == "error":
                error_text = event[1]
                self._append_log(f"Error: {error_text}")
                messagebox.showerror("Benchmark failed", error_text)
            elif kind == "finished":
                self.progress.stop()
                self.status_var.set("Ready")
                self.start_btn.configure(state=tk.NORMAL)

        if self.worker_thread and self.worker_thread.is_alive():
            self.after(100, self._poll_events)


def main() -> None:
    app = BenchmarkApp()
    app.mainloop()


if __name__ == "__main__":
    mp.freeze_support()
    main()
