---
title: How to Set Decimals for Precision
description: Learn how to control the precision in Timer for Python from 0 to 9 decimals. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# How to Use Decimals for Precision
To set the number of decimals in the output, use the `decimals` parameter. Instead of the default value `2` for `decimals`, you can set the output precision up to `9` in the `decimals` parameter:

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer(decimals=5):
    # Insert your code here
```

How it appears in the terminal:

```text title=""
Elapsed time: 0.12345 seconds
```

## Configuration Options
Default value for `decimals` is `2`. The range is minimum `0` for no decimals and up to `9`:

| Decimals | Example Output |
| --- | --- |
| `0` | 12 seconds |
| `1` | 12.3 seconds |
| `2` (default) | 12.34 seconds |
| `3` | 12.345 seconds |
| ... | ...
| `9` | 12.345678901 seconds |

!!! info "Humanised Output"
    When you measure time in microseconds, decimal precision may be important. But if a program runs for a minute or more, it doesn't make sense to display the output time in milliseconds. Therefore, the decimal configuration will be overridden in certain cases by [humanised output](humanised-output.md).

## Basic Usage
To set the number of decimals in the output (only if less than an hour), use the `decimals` parameter. Instead of the default value `2` for `decimals`, you can set the output precision up to `9` in the `decimals` parameter:

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer(decimals=5):
    # Insert your code here
```

Terminal output example:

```text title=""
Elapsed time: 0.12345 seconds
```

Or without with the `with` statement for [context management](context-manager.md):

```python linenums="1" hl_lines="4"
from timer import Timer

timer = Timer()
timer.start(decimals=5)

# Insert your code here

timer.stop()
```

Terminal output is the same:

```text title=""
Elapsed time: 0.12345 seconds
```

## Different Decimals for Different Threads
### General Configuration
It's also possible to set the decimals when initiating the Timer:

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer(decimals=5):
    # Insert your code here
```

Terminal output example:

```text title=""
Elapsed time: 0.12345 seconds
```

Or without with the `with` statement for [context management](context-manager.md):

```python linenums="1" hl_lines="3"
from timer import Timer

timer = Timer(decimals=5)
timer.start()

# Insert your code here

timer.stop()
```

Terminal output is the same:

```text title=""
Elapsed time: 0.12345 seconds
```

### How to Bypass General Configuration and Set Decimals by Thread
Or set the decimals when starting a new thread, which will also override the general decimals defined when initiating the Timer:

```python linenums="1" hl_lines="3 4"
from timer import Timer

timer = Timer(decimals=5)
timer.start(decimals=9)

# Insert your code here

timer.stop()
```

Terminal output example:

```text title=""
Elapsed time: 0.123456789 seconds
```

!!! info "Precision in Nanoseconds"
    Timer for Python uses the native `time.perf_counter_ns()` function for maximum resolution in nanoseconds.
