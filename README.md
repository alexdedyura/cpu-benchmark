# cpu-benchmark

Info:
- CPU benchmark by calculating Pi, powered by Python 3.

Algorithm
- The program calculates pi with an accuracy of 10,000 decimal places. The time spent on the calculation is counted as the test result. The result is determined by the average of 10 attempts. Lower is Better.

Supported architectures:
- x86 (AMD, Intel)
- ARM (Apple Silicon, Raspberry Pi, Qualcomm and etc)
- VLIW* (МЦСТ Эльбрус)
- RISC-V*

## How to install
### Install Python 3 from official website (Current)

https://www.python.org/downloads/

### Install cpuinfo
```bash
pip install py-cpuinfo
```

## Benchmark

```bash
python cpu-benchmark.py
```

## Benchmark Results
| CPU | Arch |  OS | Perfomance (Avg.) |
|--|--|--|--|
| Apple M1 | ARM | macOS 11.5.2 | 19.534s ✅ |
| Intel Core i3-8100 | x86 | Windows 10 20H2 | 30.636s ✅ |
| Intel Xeon Gold 6125 | x86 | Linux (Hyper-V) | 30.781s ✅ |
