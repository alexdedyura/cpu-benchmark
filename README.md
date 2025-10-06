<h1 align="center">CPU Benchmark</h1>

<p align="center">
  <img src="assets/favicon/cpu.svg" alt="cpu-logo" width="120px" height="120px"/>
    <br>
    <i>My benchmark allows you to find out the performance of your processor. The program performs math operations with pi to an accuracy of 10,000 decimal places. The time spent on the calculation is counted as the test result. The result is determined by the average of 10 attempts. Powered by Python3. Lower is better. The benchmark is calculated on both single core/thread and multicore for comparison.</i>
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

## Benchmark Results (single core)
| CPU | Arch |  OS | Perfomance (Avg.) | Verified |
|--|--|--|--|--|
| Apple M1 | ARM | macOS 11.5.2 | 19.534s | ✅ |
| Apple M1 Max | ARM | macOS 14.2.1 | 18.282s | ✅ |
| Apple M2 | ARM | macOS 13.2 | 14.779s | ✅ |
| Apple M2 Max (Mac14,13) | ARM | macOS 15.2 | 16.771s | ✅ |
| Apple M3 | ARM | macOS 23.5.0 | 20.560s | ✅ |
| Apple M3 Pro | ARM | macOS 14.2.1 | 13.345s | ✅ |
| Apple M3 Max | ARM | macOS 14.7 | 13.757s | ✅ |
| Apple M3 Max (Mac15,8) | ARM | macOS 15.2 | 15.266s | ✅ |
| Apple M4 | ARM | iPadOS 17.5 | 12.241s | ✅ |
| Apple M4 Pro | ARM | macOS 24.1.0 | 11.617s | ✅ |
| Apple M4 Max | ARM | macOS | 12.144s | ✅ |
| AMD Ryzen 9950X | x86 | Proxmox VE 8.1.4 (Debian 12) | 5.637s | ✅ |
| AMD Ryzen 7945HX | x86 | Windows 11 24H2 | 9.366s | ✅ |
| AMD Ryzen 5800H | x86 | Arch Linux | 15.906s | ✅ |
| AMD Ryzen 5800X | x86 | Windows 11 22H2 | 16.389s | ✅ |
| AMD Ryzen 5800X | x86 | Proxmox VE 8.1 (Debian 12) | 13.279s | ✅ |
| AMD Ryzen 5900HX | x86 | Unknown | 17.352s | ✅ |
| AMD Ryzen 4600H | x86 | Ubuntu 24.04.2 | 14.706s | ✅ |
| AMD Ryzen 4300GE | x86 | Linux | 40.189s | ✅ |
| AMD Ryzen 7 4800H | x86 | Windows 11 | 16.386s | ✅ |
| AMD Epyc 42444P | x86 | Windows Server 2025 | 13.985s | ✅ |
| Intel Core i3-3337U | x86 | Ubuntu 22.04 LTS | 38.576s | ✅ |
| Intel Core i3-8100 | x86 | Windows 10 20H2 | 30.636s | ✅ |
| Intel Core i3-1115G4 | x86 | Arch Linux | 17.414s | ✅ |
| Intel Core i7-1165G7 | x86 | Ubuntu 20.04.6 LTS | 16.885s | ✅ |
| Intel Core i3-12400 | x86 | Proxmox VE 8.2 (Debian 12) | 10.774s | ✅ |
| Intel Core Ultra 5 226V | x86 | Windows 11 | 13.169 | ✅ |
| Intel Core i3-3337U | x86 | Ubuntu 22.04 LTS | 38.576s | ✅ |
| Intel Xeon E5 2683 v4 | x86 | Proxmox VE 8.1 (Debian 12) | 28.596s | ✅ |
| Intel Xeon E5 2236 | x86 | Windows Server 2022 | 26.702s | ✅ |
| Intel Xeon Gold 6125 | x86 | Linux (Hyper-V Server) | 30.781s | ✅ |
| Intel Pentium Dual-Core E6700 | x86 | Linux | 41.714s | ✅ |
| Raspberry Pi 4 | ARM | Ubuntu 22.04.3 LTS | 79.216s | ✅ |
| Intel Xeon E5-2630 v4 | x86 | Windows Server 2012 | 49.883s | ✅ |
| Neoverse N1 | ARM | Linux Ubuntu 20.04 | 35.366s | ✅ |
| Huawei Kunpeng 920 | ARM | Linux | 79.399s | ✅ |
| Snapdragon 8 Gen 1 | ARM | Linux | 40.789s | ✅ |
| Snapdragon 625 | ARM | Linux | 149.585s | ✅ |
| Docker on RPI 3B | ARM | Linux | 126.469s | ✅ |
| Docker on Apple M1 | ARM | Linux | 18.98s | ✅ |
| WSL2 on AMD Ryzen Threadripper 3960X | x86_64 | Windows | 14.522s | ✅ |
| 12th Gen Intel Core i3-1210U | x86_64 | Windows | 47.053s | ✅ |


