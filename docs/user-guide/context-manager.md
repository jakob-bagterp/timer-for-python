---
tags:
    - Features
    - Tutorial
---

# Context Management
## How to Automatically Start and Stop the Timer
Instead of manually starting and stopping the Timer with `timer.start()` and `timer.stop()`, it's recommend to use the context manager and `with Timer():` statements.

### Advantages
Apart from less code and more readable code, the built-in context manager automatically closes the Timer (so you don't forget it) when the task is done or if an error occurs.

As an added benefit, the `with` statement prevents you from having loose ends lingering in the Python runtime.

## Examples
### With Context Manager
It's recommended to do this:

```python linenums="1" hl_lines="3"
from timer import Timer

with Timer():
    # Insert your code here
```

### Without Context Manager
And not recommended to do this:

```python linenums="1"
from timer import Timer

timer = Timer()
timer.start()

# Insert your code here

timer.stop()
```

## Multiple Threads and Decimals
It's possible nest multiple instances of context. Simply remember to add a unique `thread` argument to each instance of `Timer()`.

```python linenums="1" hl_lines="3 6 9"
from timer import Timer

with Timer(thread="A")
    # Insert your code here

    with Timer(thread="B", decimals=5):
        # Insert more code here

    with Timer(thread="C", decimals=3):
        # Insert even more code here

    # Insert even more code here for thread A
```

```text title=""
0.12345 seconds for thread B
0.123 seconds for thread B
1.23 seconds for thread A
```

Learn more about [decimals](decimals.md) and [threads](multiple-threads.md).

!!! info "Singleton and Unique Threads"
    The `Timer()` class is a singleton, which means that there can only be one instance of the class. This is to ensure that the same `Timer()` is used for all threads and that each thread is unique.
