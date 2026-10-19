# CLAUDE.md

Public open-source CPU benchmark (`github.com/alexdedyura/cpu-benchmark`,
GPL-3.0): a fixed float workload around pi (`_workload` in
`benchmark_core.py`, 10,000 iterations), averaged over 10 runs, single core and
all cores; lower is better. User docs and the results tables: [README.md](README.md).

## Layout

| File | What |
|---|---|
| `benchmark_core.py` | the only benchmark logic: `BenchmarkConfig`, `run_single_core`, `run_multi_core`, `run_full_benchmark`, `get_system_info` |
| `cpu-benchmark.py` | CLI frontend |
| `cpu-benchmark-ui.py` | Tkinter GUI frontend (Windows, macOS, Linux) |
| `cpuinfo.py` | **vendored** py-cpuinfo 9.0.0 (third-party, own copyright header) |

Both frontends import from `benchmark_core.py`; keep it the single place for
the algorithm and timing, so CLI and GUI results stay comparable.

## Rules

- **Stdlib only.** The README promises "install Python 3 and run": no
  `requirements.txt`, no pip dependencies. Tkinter is the only GUI toolkit.
- **Do not change the workload** (iterations, repeats, the math itself)
  without the owner's explicit decision: every row in the README results tables
  was measured with it, and a change invalidates them all.
- `cpuinfo.py` is vendored: update it only as a whole upstream release, never
  patch it in place. Its import is guarded in `benchmark_core.py` because
  py-cpuinfo raises a bare `Exception` at import on unknown architectures
  (RISC-V); CPU detection must stay non-fatal.
- Results tables in the README come from contributors via pull requests;
  keep their columns and sort order, mark unverified rows as such.

## Run and check

```bash
python3 cpu-benchmark.py        # CLI
python3 cpu-benchmark-ui.py     # GUI
python3 -m py_compile benchmark_core.py cpu-benchmark.py cpu-benchmark-ui.py
```

There are no tests and no CI. A full run takes minutes — for a quick check,
call the core with a smaller `BenchmarkConfig` from a scratch script instead of
editing the defaults.

## Workflow

GitHub, not the homelab GitLab: a branch (`fix/…`, `feat/…`) and a pull request
into `main`; commit messages in English, `<type>: description`. The repository
is public — no homelab hostnames, IPs or personal data in code or docs.
