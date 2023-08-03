---
tags:
    - Features
---

# Multiple Threads
Imagine that you want to troubleshoot which parts of your code are performing better or worse? Or you want to split test the performance of different methods? Timer for Python is a quick, easy way to get the job done.

## Code Exmaple
To measure performance of multiple blocks of code, use the `thread` argument to name different threads:

```python linenums="1" hl_lines="4 8 12 16"
from timer import Timer

timer = Timer()
timer.start(thread="A")

# Insert your code here

    timer.start(thread="B", decimals=5)

    # Insert more code here

    timer.stop(thread="B")

# Insert even more code here

timer.stop(thread="A")
```

Terminal output example:

```text title=""
0.12345 seconds for thread B
6.78 seconds for thread A
```

## Context Manager
Or use the context manager `with` statement to get the same result with less code:

```python linenums="1" hl_lines="3 6"
from timer import Timer

with Timer(thread="A")
    # Insert your code here

    with Timer(thread="B", decimals=5):
        # Insert more code here

    # Insert even more code here
```

!!! info "Singleton and Unique Threads"
    The `Timer()` class is a singleton, which means that there can only be one instance of the class. This is to ensure that the same `Timer()` is used for all threads and that each thread is unique.
