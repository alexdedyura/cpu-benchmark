<h1 align="center">CPU Benchmark</h1>

<p align="center">
  <img src="assets/favicon/cpu.svg" alt="cpu-logo" width="120px" height="120px"/>
  <br>
  <i>My benchmark allows you to find out the performance of your processor. The program calculates pi with an accuracy of 10,000 decimal places. The time spent on the calculation is counted as the test result. The result is determined by the average of 10 attempts. Powered by Python3. Lower is Better.</i>
  <br>
</p>

Supported architectures:
- x86 (AMD, Intel)
- ARM (Apple Silicon, Raspberry Pi, Qualcomm and etc)
- RISC-V*

## How to install
### Install Python 3 from official website (Current)

https://www.python.org/downloads/

### Clone repository and entering directory
```bash
git clone https://github.com/alexdedyura/cpu-benchmark
cd cpu-benchmark
```

## Benchmark

```bash
python cpu-benchmark.py or python3 cpu-benchmark.py
```

## Benchmark Results
| CPU | Arch |  OS | Perfomance (Avg.) | Verified |
|--|--|--|--|--|
| Apple M1 | ARM | macOS 11.5.2 | 19.534s | ✅ |
| Apple M1 Max | ARM | macOS 14.2.1 | 18.282s | ✅ |
| Apple M2 | ARM | macOS 13.2 | 14.779s | ✅ |
| Apple M3 Pro | ARM | macOS 14.2.1 | 13.345s | ✅ |
| AMD Ryzen 5800H | x86 | Arch Linux | 15.906s | ✅ |
| AMD Ryzen 5800X | x86 | Windows 11 22H2 | 16.389s | ✅ |
| AMD Ryzen 5800X | x86 | Proxmox VE 8.1 (Debian 12) | 13.279s | ✅ |
| AMD Ryzen 5900HX | x86 | Unknown | 17.352s | ✅ |
| AMD Ryzen 4300GE | x86 | Linux | 40.189s | ✅ |
| Intel Core i3-3337U | x86 | Ubuntu 22.04 LTS | 38.576s | ✅ |
| Intel Core i3-8100 | x86 | Windows 10 20H2 | 30.636s | ✅ |
| Intel Core i3-1115G4 | x86 | Arch Linux | 17.414s | ✅ |
| Intel Xeon E5 2683 v4 | x86 | Proxmox VE 8.1 (Debian 12) | 28.596s | ✅ |
| Intel Xeon Gold 6125 | x86 | Linux (Hyper-V Server) | 30.781s | ✅ |
| Intel Pentium Dual-Core E6700 | x86 | Linux | 41.714s | ✅ |
| Raspberry Pi 4 | ARM | Ubuntu 22.04.3 LTS | 79.216s | ✅ |
| Intel Xeon E5-2630 v4 | x86 | Windows Server 2012 | 49.883s | ✅ |
| Neoverse N1 | ARM | Linux (Ubuntu 20.04, 4 threads) | 35.366s | ✅ |
| Huawei Kunpeng 920 | ARM | Linux | 79.399s | ✅ |
| Snapdragon 8 Gen 1 | ARM | Linux | 40.789s | ✅ |
| Docker on RPI 4 | ARM | Linux | 126.469s | ✅ |
| Docker on Apple M1 | ARM | Linux | 18.98s | ✅ |


