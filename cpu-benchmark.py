#!/usr/bin/python3
# Python CPU Benchmark by Alex Dedyura (Windows, macOS, Linux)

import platform
import time

import cpuinfo

os_version = platform.system()

print("Python CPU Benchmark by Alex Dedyura (Windows, macOS(Darwin), Linux)")
print("CPU: " + cpuinfo.get_cpu_info().get("brand_raw", "Unknown"))
print("Arch: " + cpuinfo.get_cpu_info().get("arch_string_raw", "Unknown"))
print("OS: " + str(os_version))

print("\nBenchmarking: \n")

start_benchmark = 10000  # change this if you like (sample: 1000, 5000, etc)
start_benchmark = int(start_benchmark)

repeat_benchmark = 10  # attemps, change this if you like (sample: 3, 5, etc)
repeat_benchmark = int(repeat_benchmark)

average_benchmark = 0

for a in range(0, repeat_benchmark):

    start = time.perf_counter()

    for i in range(0, start_benchmark):
        for x in range(1, 1000):
            3.141592 * 2**x
        for x in range(1, 10000):
            float(x) / 3.141592
        for x in range(1, 10000):
            float(3.141592) / x

    end = time.perf_counter()
    duration = end - start
    duration = round(duration, 3)
    average_benchmark += duration
    print("Time: " + str(duration) + "s")

average_benchmark = round(average_benchmark / repeat_benchmark, 3)
print("Average (from 10 repeats): " + str(average_benchmark) + "s")
