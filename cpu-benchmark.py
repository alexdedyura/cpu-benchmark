#!/usr/bin/python3
#Python CPU Benchmark by Alex Dedyura (Windows, macOS, Linux)

import time
import platform
import cpuinfo

print('Python CPU Benchmark by Alex Dedyura (Windows, macOS(Darwin), Linux)')
print('CPU: ' + cpuinfo.get_cpu_info().get('brand_raw', "Unknown"))
print('Arch: ' + cpuinfo.get_cpu_info().get('arch_string_raw', "Unknown"))
print('OS: ' + platform.system(), platform.release())
print('Python: ' + platform.python_version())

print('\nBenchmarking: \n')

start_benchmark = 10000  # The number of iterations in each test
repeat_benchmark = 10    # The number of repetitions of the test

# Initializing a variable to accumulate execution time
total_duration = 0

# Starting the test cycle
for attempt in range(repeat_benchmark):
    start = time.perf_counter()  # Recording the initial time
    
    # Nested loops for performing calculations
    for i in range(start_benchmark):
        for x in range(1, 1000):
            3.141592 * 2 ** x  # Multiplying the number Pi by 2 to the power of xx
        for x in range(1, 10000):
            float(x) / 3.141592  # Dividing x by Pi
        for x in range(1, 10000):
            float(3.141592) / x  # Dividing the number Pi by x
    
    end = time.perf_counter()  # Recording the end time
    duration = round(end - start, 3)  # Calculate and round up the execution time
    total_duration += duration  # Adding the execution time to the total amount
    print(f'Time: {duration}s')  # We output the execution time for each iteration

# Calculate and output the average execution time
average_duration = round(total_duration / repeat_benchmark, 3)
print(f'Average (from {repeat_benchmark} repeats): {average_duration}s')