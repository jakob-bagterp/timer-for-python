[![Latest version](https://img.shields.io/static/v1?label=version&message=v0.3.4&color=yellowgreen)](https://github.com/jakob-bagterp/timer-for-python/releases)
![Python 3.9](https://img.shields.io/static/v1?label=python&message=v3.9&color=green)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/timer-for-python/blob/master/LICENSE.md)

# Timer for Python
Timer for Python makes it easy to measure how much time it takes to run Python programs and gauge performance of multiple, smaller bits of code.

## Prerequisites
* Python 3.9 or higher
* macOS
    * It may work on Windows or Linux, but hasn't been tested

## Installation
### PyPI
```shell
pip3 install timer-for-python
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, use this terminal command to tap Timer for Python:

```shell
brew tap jakob-bagterp/timer-for-python
```

And then install:

```shell
brew install timer-for-python
```

### NuGet
TBC

## Getting Started
### Basic
Firstly, add the Timer to your imports:

```python
from timer import Timer
```

Wrap the Timer function around your code to measure performance of the executed block of code:

```python
timer = Timer()
timer.start()

# Insert your code here

timer.stop() # Output example: 12.34 seconds
```

### Advanced
#### Decimals
Instead of the default value `2` for `decimals`, you can set the output precision up to `9` in the `decimals` argument:

```python
timer = Timer()
timer.start(decimals = 5)

# Insert your code here

timer.stop() # Output example: 0.12345 seconds
```

#### Multiple Threads
Imagine that you want to troubleshoot which parts of your code are performing better or worse? Or you want to split test the performance of different methods? Timer for Python is a quick, easy way to get the job done.

To measure performance of multiple blocks of code, use the `thread` argument to name different threads:

```python
timer = Timer()
timer.start(thread = "A")

# Insert your code here

    timer.start(thread = "B", decimals = 5)

    # Insert more code here

    timer.stop(thread = "B") # Output example: 0.12345 seconds for thread B

# Insert even more code here

timer.stop(thread = "A")  # Output example: 6.78 seconds for thread A
```

## Documentation and Other Features
### Precision in Nanoseconds
Timer for Python uses the native `time.perf_counter_ns()` function for maximum resolution in nanoseconds.

### Decimals in Output
To set the number of decimals in the output (only if less than an hour), use the `decimals` argument.

Either, set the general precision of decimals when initiating the Timer:

```python
timer = Timer(decimals = 5)
timer.start()

# Insert your code here

timer.stop() # Output example: 0.12345 seconds
```

Or set the decimals when starting a new thread, which will also override the general decimals defined when initiating the Timer:

```python
timer = Timer(decimals = 5)
timer.start(decimals = 9)

# Insert your code here

timer.stop() # Output example: 0.123456789 seconds
```

#### Default Decimals and Supported Interval
Default value for `decimals` is `2`. The range is minimum `0` (for no decimals) and up to `9`.

### Humanised Output
Timer for Python supports time measurement from nanoseconds to days.

But. If the Timer runs for several minutes, it doesn't make sense to display the output time in milliseconds. And similarly if it runs for hours, it doesn't make sense to display the output time in seconds.

Therefore, the output is "humanised" so it's easier to read. Examples:

```
Elapsed time: 123 nanoseconds
Elapsed time: 4.56 microseconds
Elapsed time: 56.78 milliseconds
Elapsed time: 7.89 seconds
Elapsed time: 67.89 seconds (1m 8s)
Elapsed time: 3m 4s
Elapsed time: 2h 3m 4s
Elapsed time: 1d 2h 3m 4s
```

### Graceful Error Handling
Timer for Python is designed with several nested `try/catch` clauses so it handles exceptions gracefully and therefore shouldn't break your application while running. However, if you find a bug, please [report it](https://github.com/jakob-bagterp/timer-for-python/issues).

## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/timer-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/timer-for-python/issues).
