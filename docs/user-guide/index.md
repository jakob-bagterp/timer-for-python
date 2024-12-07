---
atitle: User Guide to Start, Stop and Measure Time
description: Get the most out of Timer for Python's many features with comprehensive tutorials, tips, and tricks. Includes guides and code examples for both beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# User Guide 👨‍🔧
Timer for Python is a lightweight package and intended to be easy to use. A simple tool for measuring performance of Python programs or blocks of code.

Find tutorials and learn how get the most out of the Timer in this section.

## Basic Usage and How to Wrap Your Code
### Manual Start and Stop
After importing the Timer on top of your Python script, simply wrap the Timer function around your code to measure performance of the executed block of code:

```python linenums="1" hl_lines="3-4 8"
from timer import Timer

timer = Timer()
timer.start()

# Insert your code here

timer.stop()
```

After `timer.stop()`, the elapsed time will be printed in the terminal:

```text title=""
% Elapsed time: 12.34 seconds
```

### Automatic Start and Stop
Alternatively, use the `with` statement for [context management](context-manager.md). This will automatically start and stop the Timer – and so no need to declare `timer.start()` and `timer.stop()`. Same result as before, but less code:

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer():
    # Insert your code here
```

How it appears in the terminal:

```text title=""
% Elapsed time: 12.34 seconds
```

### Decimals
Set [decimals](decimals.md) to customise the precision of the terminal output:

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer(decimals=5):
    # Insert your code here
```

How it appears in the terminal:

```text title=""
% Elapsed time: 0.12345 seconds
```

### Multiple Threads
There's total flexibility to measure the performance of different blocks of code using [multiple threads](user-guide/multiple-threads.md):

```python linenums="1" hl_lines="3 6"
from timer import Timer

with Timer(thread="A")
    # Insert your code here

    with Timer(thread="B", decimals=5):
        # Insert more code here

    # Insert even more code here
```

How it appears in the terminal:

<pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">B</span>
% Elapsed time: 6.78 seconds for thread <span class="fg-green">A</span></code></pre>

## Quick Links
* [Multiple threads](multiple-threads.md) to measure the performance of different blocks of code
* [Decimals](decimals.md) to set the precision of the terminal output
* [Context manager](context-manager.md) to automatically start and stop the Timer
* [Function decorator](function-decorator.md) to measure the performance of functions
* [Humanised output](humanised-output.md) to display time measurements in human-readable format
* [Graceful error handling](graceful-error-handling.md) to gracefully handle exceptions and non-blocking code

## Support the Project

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
