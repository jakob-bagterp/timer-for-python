---
title: The Easy Way to Measure Start and Stop Time with Python
description: Learn how to measure elapsed time of your Python code like a stop watch. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
    - Start Timer
    - Stop Timer
---

# How to Start and Stop Time Measurements with Python
Instead of using Timer for Python, you can also make your own performance timer.

## Adding a Stop Watch to Your Code
Python has different methods to measurement time as a stop watch. The most common is the [`time` standard library](https://docs.python.org/3/library/time.html), and this will be sufficient for most use cases.

But if you want higher precision, you can use the out-of-the box methods [`perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter) or [`perf_counter_ns`](https://docs.python.org/3/library/time.html#time.perf_counter_ns). Both part of the `time` standard library, so you don't need to install anything beyond a Python interpreter.

### Overview of Different Methods
Here's a comparison of different time measurement methods from the standard librray:

| Method              | Description                                                                                                                                                           | Returns           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `time()`            | Basic time measurement with system clock resolution. Suitable for general timing needs. Less precise as it can be affected by system clock updates.                   | `float` seconds   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `perf_counter()`    | High-resolution performance counter for benchmarking. Most suitable for measuring elapsed time. Returns floating-point seconds. Not affected by system clock updates. | `float` seconds   |
| `perf_counter_ns()` | Similar to `perf_counter()`, but returns nanoseconds as integer. Highest precision timing available in Python. Best for very precise measurements.                    | `int` nanoseconds |

## Basic Examples
Each method follows the same pattern:

1. Start the timer
2. Execute the code
3. Stop the timer
4. Calculate the elapsed time

The main differences are in the precision and units of the returned values. Please try the following different methods to start and stop time to see what works best for you:

### Using `time()`
```python linenums="1" hl_lines="3 7-8"
from time import time

start_time = time()

# Insert your code here

end_time = time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
```

### Using `perf_counter()`
```python linenums="1" hl_lines="3 7-8"
from time import perf_counter

start_time = perf_counter()

# Insert your code here

end_time = perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
```

### Using `perf_counter_ns()`
```python linenums="1" hl_lines="3 7-8"
from time import perf_counter_ns

start_time = perf_counter_ns()

# Insert your code here

end_time = perf_counter_ns()
elapsed_time_ns = end_time - start_time

print(f"Elapsed time: {elapsed_time_ns} nanoseconds")

elapsed_time = elapsed_time_ns / 1_000_000_000
print(f"Elapsed time: {elapsed_time:.2f} seconds")
```

### Using Timer for Python
Alternatively, you can achieve the same result with Timer for Python using less code. Simply wrap the Timer around the code you want to measure. This can be done with or without the `with` statement for [context management](../context-manager.md):

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer():
    # Insert your code here
```

Or use the `@function_timer()` as [function decorator](../function-decorator.md) to measure the performance of a function:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer()
def test_function():
    # Insert your code here

test_function()
```

## Advanced Examples
### Calculate the Average of Multiple Runs
Imagine you want to measure the performance of a function. Since each run may vary from run to run, let's calculate the average execution time of the function across multiple runs.

Here's a simple example:

```python linenums="1"
from time import perf_counter

def function_to_measure():
    sum([i * i for i in range(1_000)])

runs = 1_000
measurements = []

for _ in range(runs):
    start = perf_counter()
    function_to_measure()
    end = perf_counter()
    elapsed_time = end - start
    measurements.append(elapsed_time)

average_time = sum(measurements) / len(measurements)
min_time = min(measurements)
max_time = max(measurements)

print(f"Average time: {average_time:.6f} seconds")
print(f"Min time: {min_time:.6f} seconds")
print(f"Max time: {max_time:.6f} seconds")
```
