---
title: How to Use Timer as Function Decorator
description: Tutorial on how to use the timer as function decorator to measure the execution time of Python functions. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# Function Decorator
## What Is a Decorated Function?
The `@` preceding a function is called a decorator. Such decoractor wraps a function and gives extra functionality without changing the original function.

The pattern is:

```python title=""
@decorator
def function():
    # Function code
```

## Example
### Basic Usage
Use the `@function_timer()` as decorator to measure performance time of a function:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer()
def test_function():
    # Insert your code here

test_function()
```

Terminal output example:

```text title=""
Elapsed time: 12.34 seconds for thread TEST_FUNCTION
```

### Custom Thread Name and Decimals
Similar to customising [output decimals](decimals.md) and [thread name](multiple-threads.md) for the Timer, this is also possible with the `@function_timer()` decorator. Simply use the `thread` and `decimals` arguments:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer(thread="A", decimals=5)
def test_function():
    # Insert your code here

test_function()
```

Terminal output example:

```text title=""
Elapsed time: 0.12345 seconds for thread A
```
