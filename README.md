<h1 align="center">CPU Benchmark</h1>

<p align="center">
  <img src="assets/favicon/cpu.svg" alt="angular-logo" width="120px" height="120px"/>
  <br>
  <i>My benchmark allows you to find out the performance of your processor. The program calculates pi with an accuracy of 10,000 decimal places. The time spent on the calculation is counted as the test result. The result is determined by the average of 10 attempts. Powered by Python3. Lower is Better.</i>
  <br>
</p>

Supported architectures:
- x86 (AMD, Intel)
- ARM (Apple Silicon, Raspberry Pi, Qualcomm and etc)
- VLIW* (МЦСТ Эльбрус)
- RISC-V*

## How to install
### Install Python 3 from official website (Current)

https://www.python.org/downloads/

### Clone repository and entering directory
```bash
git clone https://github.com/alexdedyura/cpu-benchmark
cd cpu-benchmark
```

### Install cpuinfo
```bash
pip install py-cpuinfo
```

## Benchmark

```bash
python cpu-benchmark.py
```

## Benchmark Results
| CPU | Arch |  OS | Perfomance (Avg.) | Verified |
|--|--|--|--|--|
| Apple M1 | ARM | macOS 11.5.2 | 19.534s | ✅ |
| Intel Core i3-8100 | x86 | Windows 10 20H2 | 30.636s | ✅ |
| Intel Xeon Gold 6125 | x86 | Linux (Hyper-V) | 30.781s | ✅ |
