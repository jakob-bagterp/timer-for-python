---
title: How to Use Timer as Function Decorator
description: Tutorial on how to use the timer as function decorator to measure the execution time of Python functions. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# How to Measure Time of Functions
When you want to measure the performance of a function, use the function decorator.

## Example
Use the `@function_timer` as function decorator to measure performance time:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer
def test_function():
    # Insert your code here

test_function()
```

Terminal output example:

```text title=""
Elapsed time: 12.34 seconds for thread TEST_FUNCTION
```

## What Is a Decorated Function?
The `@` preceding a function is called a decorator. Such decoractor wraps a function and gives extra functionality without changing the original function.

The pattern is:

```python title=""
@decorator
def some_function():
    # Function code
```
