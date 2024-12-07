---
title: How Measure Time with Multiple Threads
description: Learn how to measure the time and performance of different blocks of code using multiple threads. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# Why Use Multiple Threads?
Imagine that you want to troubleshoot which parts of your code are performing better or worse. Or do you want to split-test the performance of different methods? Timer for Python is a quick, easy way to get the job done.

## Code Exmaple
To measure the performance of multiple blocks of code, use the `thread` parameter to name different threads:

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

How it appears in the terminal:

<pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">B</span>
% Elapsed time: 6.78 seconds for thread <span class="fg-green">A</span></code></pre>


## Context Manager
Or use the [context manager](context-manager.md) `with` statement to get the same result with less code:

```python linenums="1" hl_lines="3 6"
from timer import Timer

with Timer(thread="A")
    # Insert your code here

    with Timer(thread="B", decimals=5):
        # Insert more code here

    # Insert even more code here
```

Learn more about [context management](context-manager.md).

!!! info "Singleton and Unique Threads"
    The `Timer()` class is a _singleton_, which means that there can only be one instance of the class. This is to ensure that the same `Timer()` is used for all threads and that each thread is unique.
