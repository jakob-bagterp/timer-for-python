---
tags:
    - Features
    - Tutorial
---

# User Guide 👨‍🔧
Timer for Python is a lightweight package and intended to be easy to use. A simple tool for measuring performance of Python programs or blocks of code.

## Basics
### Define Imports
Firstly, import the Timer on top of your Python script:

```python linenums="1"
from timer import Timer

```

### Wrap Your Code with Start and Stop
Wrap the Timer function around your code to measure performance of the executed block of code:

```python linenums="3" hl_lines="4"
timer = Timer()
timer.start()

# Insert your code here

timer.stop()
```

After `timer.stop()`, the elapsed time will be printed in your terminal. Example:

```text title=""
Elapsed time: 12.34 seconds
```

## Core Features
When the basics aren't sufficient, Timer for Python also offers more advanced features to measure performance of specific code blocks:

* threads,
* function decorators,
* and more.

A few excerpts:

### Multiple Threads
Set [multiple threads](multiple-threads.md) to measure performance of different blocks of code:

```python title=""
timer.start(thread="A") >-------|
# Insert your code here         |
                                |
timer.start(thread="B") >---|   |
for i in range(100):        |   |
    # Insert more code here |   |
timer.stop(thread="B") <----|   |
                                |
timer.stop(thread="A") <--------|
```

### Decimals
Set [decimals](decimals.md) to customise the precision of the terminal output:

```python title=""
timer.start(decimals=5)
```

### Context Manager
Avoid using `start()` and `stop()` by applying the built-in [context manager](context-manager.md) `with` statement. This can be used in combination with decimals and multiple threads:

```python title=""
with Timer(thread="A"): >----------------------|
    # Insert your code here                    |
                                               |
    with Timer(thread="B", decimals=5): >--|   |
        # Insert more code here            |   |
        |<---------------------------------|   |
    |<-----------------------------------------|
```

### Function Decorator
How to apply the [function decorator](function-decorator.md) to measure performance of functions:

```python title=""
@benchmark_timer
def some_function():
    # Function code
```
