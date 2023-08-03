---
tags:
    - Features
    - Tutorial
---

# User Guide 👨‍🔧
Timer for Python is intended to lightweight and easy to use. A simple tool for measuring performance of Python programs or blocks of code.

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

## Advanced Features
When the basics aren't sufficient, Timer for Python also offers more advanced features to measure performance of specific code blocks with threads, function decorators, and more. A few excerpts:

### Multiple Threads
Set [multiple threads](multiple-threads.md) to measure performance of different blocks of code:

```python title=""
timer.start(thread="A")
# Insert your code here
timer.start(thread="B")
# Insert more code here
timer.stop(thread="B")
timer.stop(thread="A")
```

### Decimals
Set [decimals](decimals.md) to customise the precision of the terminal output:

```python title=""
timer.start(decimals=5)
```

### Context Manager
Avoid using `start()` and `stop()` by applying the built-in [context manager](context-manager.md) `with` statement. This can be used in combination with decimals and multiple threads:

```python title=""
with Timer(thread="A"):
    # Insert your code here
    with Timer(thread="B", decimals=5):
    # Insert more code here
```

### Function Decorator
Use the [function decorator](function-decorator.md) to measure performance of functions:

```python title=""
@benchmark_timer
def some_function():
    # Function code
```
