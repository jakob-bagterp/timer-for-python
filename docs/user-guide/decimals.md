---
title: How to Set Decimals for Precision
description: Learn how to control the precision in Timer for Python from 0 to 9 decimals. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# Decimals
## How to Use
To set the number of decimals in the output (only if less than an hour), use the `decimals` argument. Instead of the default value `2` for `decimals`, you can set the output precision up to `9` in the `decimals` argument:

```python linenums="1" hl_lines="4"
from timer import Timer

timer = Timer()
timer.start(decimals=5)

# Insert your code here

timer.stop()
```

Terminal output example:

```text title=""
Elapsed time: 0.12345 seconds
```

!!! info "Default Decimals and Supported Interval"
    Default value for `decimals` is `2`. The range is minimum `0` (for no decimals) and up to `9`.

    May be overruled in certain cases due to [humanised output](humanised-output.md).

## Set Decimals in Class Instance or Function
It's also possible to set the decimals when initiating the Timer:

```python linenums="1" hl_lines="3"
from timer import Timer

timer = Timer(decimals=5)
timer.start()

# Insert your code here

timer.stop()
```

Terminal output example:

```text title=""
Elapsed time: 0.12345 seconds
```

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
