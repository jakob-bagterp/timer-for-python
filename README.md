[![Latest version](https://img.shields.io/static/v1?label=version&message=0.7.4&color=yellowgreen)](https://github.com/jakob-bagterp/timer-for-python/releases/latest)
[![Python 3.10 | 3.11 | 3.12 | 3.13+](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%20|%203.12%20|%203.13%2B&color=blueviolet)](https://www.python.org)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/timer-for-python/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/timer-for-python/branch/master/graph/badge.svg?token=P4IT8WQO0R)](https://codecov.io/gh/jakob-bagterp/timer-for-python)
[![CodeQL](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/timer-for-python)](https://pepy.tech/project/timer-for-python)

# ⏳ Timer for Python ⌛️
Lightweight Python package that makes it easy to measure how much time it takes to run Python programs and gauge performance of multiple, smaller bits of code.

Ready to try? Learn [how to install](https://jakob-bagterp.github.io/timer-for-python/getting-started/installation/) and find tutorials in the [user guide](https://jakob-bagterp.github.io/timer-for-python/user-guide/).

## Getting Started
### Basics
Simply add the Timer to your imports, and then wrap the Timer function around your code to measure the performance of the executed block of code:

```python
from timer import Timer

timer = Timer()
timer.start()

# Insert your code here

timer.stop() # Output example: 12.34 seconds
```

#### Context Manager
Alternatively, use the with statement. This will automatically start and stop the Timer – and so no need to declare `timer.start()` and `timer.stop()`. Same result as before, but less code:

```python
with Timer():
    # Insert your code here

    # Output example: 12.34 seconds
```

#### Decorator
Or use the `benchmark_timer` as a function decorator:

```python
from timer import benchmark_timer

@benchmark_timer
def test_function():
    # Insert your code here

test_function()

# Output example: 12.34 seconds for thread TEST_FUNCTION
```

### Core Features
#### Decimals
Instead of the default value of `2` for `decimals``, you can set the output precision up to `9` in the `decimals` argument:

```python
timer = Timer()
timer.start(decimals=5)

# Insert your code here

timer.stop() # Output example: 0.12345 seconds
```

#### Multiple Threads
Imagine that you want to troubleshoot which parts of your code are performing better or worse. Or do you want to split-test the performance of different methods? Timer for Python is a quick, easy way to get the job done.

To measure the performance of multiple blocks of code, use the `thread` argument to name different threads:

```python
timer = Timer()
timer.start(thread="A")

# Insert your code here

    timer.start(thread="B", decimals=5)

    # Insert more code here

    timer.stop(thread="B") # Output example: 0.12345 seconds for thread B

# Insert even more code here

timer.stop(thread="A") # Output example: 6.78 seconds for thread A
```

Or use the `with` statement to get the same result with less code:
```python
with Timer(thread="A")
    # Insert your code here

    with Timer(thread="B", decimals=5):
        # Insert more code here

        # Output example: 0.12345 seconds for thread B

    # Insert even more code here

    # Output example: 6.78 seconds for thread A
```

# Thank You for Supporting
## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/timer-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/timer-for-python/issues).
