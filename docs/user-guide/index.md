---
atitle: User Guide to Start, Stop and Measure Time
description: Get the most out of Timer for Python's many features with comprehensive tutorials, tips, and tricks. Includes guides and code examples for both beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# User Guide 👨‍🔧
Timer for Python is a lightweight package and intended to be easy to use. A simple tool for measuring performance of Python programs or blocks of code.

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

After `timer.stop()`, the elapsed time will be printed in your terminal. Example:

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

Terminal output example:

```text title=""
% Elapsed time: 12.34 seconds
```

## Key Features
When the basics aren't sufficient, Timer for Python also offers more advanced features to measure performance of specific code blocks:

* threads
* function decorators
* decimals for precision

And much more. A few excerpts:

### Decimals
Set [decimals](decimals.md) to customise the precision of the terminal output:

```python title=""
timer.start(decimals=5)
```

### Multiple Threads
Set [multiple threads](multiple-threads.md) to measure performance of different blocks of code:

```python title="" hl_lines="1 4 8 10"
timer.start(thread="A") >------------------|
# Insert your code here                    |
                                           |
timer.start(thread="B", decimals=5) >--|   |
for i in range(100):                   |   |
    # Insert more code here            |   |
                                       |   |
timer.stop(thread="B") <---------------|   |
                                           |
timer.stop(thread="A") <-------------------|
```

### Context Manager
Avoid using `start()` and `stop()` by applying the built-in [context manager](context-manager.md) `with` statement. This can be used in combination with decimals and multiple threads:

```python title="" hl_lines="1 4"
with Timer(thread="A"): >----------------------|
    # Insert your code here                    |
                                               |
    with Timer(thread="B", decimals=5): >--|   |
        # Insert more code here            |   |
        |<---------------------------------|   |
                                               |
    |<-----------------------------------------|
```

### Function Decorator
How to apply the [function decorator](function-decorator.md) to measure performance of functions:

```python title="" hl_lines="1"
@function_timer()
def some_function():
    # Function code
```

## Support the Project

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
