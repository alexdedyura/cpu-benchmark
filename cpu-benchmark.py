#!/usr/bin/python3
# Python CPU Benchmark by Alex Dedyura (Windows, macOS, Linux)

import time
import platform
import cpuinfo
import multiprocessing as mp

def single_core_benchmark(start_benchmark, repeat_benchmark):
    total_duration = 0
    print('\n--- Single-Core Benchmark ---\n')
    for attempt in range(repeat_benchmark):
        start = time.perf_counter()
        for _ in range(start_benchmark):
            for x in range(1, 1000):
                3.141592 * 2 ** x # Multiplying the number Pi by 2 to the power of x
            for x in range(1, 10000):
                float(x) / 3.141592 # Dividing x by Pi
            for x in range(1, 10000):
                float(3.141592) / x # Dividing the number Pi by x
        end = time.perf_counter() # Recording the end time
        duration = round(end - start, 3) # Calculate and round up the execution time
        total_duration += duration # Adding the execution time to the total amount
        print(f'Attempt {attempt + 1}: {duration}s')
    
    average_duration = round(total_duration / repeat_benchmark, 3)
    print(f'\nSingle-Core Average (from {repeat_benchmark} repeats): {average_duration}s\n')
    return average_duration

def multicore_worker(args):
    start_benchmark, chunk_size = args
    total_ops = 0
    start = time.perf_counter()

    for _ in range(chunk_size):
        for x in range(1, 1000):
            3.141592 * 2 ** x
        for x in range(1, 10000):
            float(x) / 3.141592
        for x in range(1, 10000):
            float(3.141592) / x
        total_ops += 1

    end = time.perf_counter()
    return round(end - start, 3), total_ops

if __name__ == '__main__':
    try:
        print('Python CPU Benchmark by Alex Dedyura (Windows, macOS (Darwin), Linux)')
        print('CPU: ' + cpuinfo.get_cpu_info().get('brand_raw', "Unknown"))
        print('Arch: ' + cpuinfo.get_cpu_info().get('arch_string_raw', "Unknown"))
        print('OS: ' + platform.system(), platform.release())
        print('Python: ' + platform.python_version())

        # Benchmark parameters
        start_benchmark = 10000  # Number of iterations per test
        repeat_benchmark = 10    # Number of repetitions per test

        # Run Single-Core Benchmark
        single_time = single_core_benchmark(start_benchmark, repeat_benchmark)
        single_ops_per_second = start_benchmark / single_time
        print(f'Single-Core Operations per second: {int(single_ops_per_second)}\n')

        # Run Multi-Core Benchmark
        print('\n--- Multicore Benchmark ---\n')
        num_cores = mp.cpu_count()
        print(f'Utilizing {num_cores} cores for benchmarking...\n')

        chunk_size = start_benchmark // num_cores
        args = [(start_benchmark, chunk_size)] * num_cores

        total_ops = 0
        start_time = time.perf_counter()

        with mp.Pool(processes=num_cores) as pool:
            results = []
            for idx, (avg, ops) in enumerate(pool.imap_unordered(multicore_worker, args), start=1):
                print(f'Core {idx} finished: {avg}s')
                results.append(avg)
                total_ops += ops

        end_time = time.perf_counter()
        total_time = round(end_time - start_time, 3)

        print(f'\nMulticore Results:')
        print(f'Total wall time: {total_time}s')
        print(f'Total operations completed: {total_ops}')
        multi_ops_per_second = total_ops / total_time
        print(f'Multi-Core Operations per second: {int(multi_ops_per_second)}')

        # Performance Comparison
        speedup = multi_ops_per_second / single_ops_per_second
        print(f'\nSpeedup vs Single-Core: {speedup:.2f}x')
    
    except KeyboardInterrupt:
        print("\nBenchmark interrupted. Exiting...")
        exit(1)
