---
title: How to Use Timer as Function Decorator
description: Tutorial on how to use the timer as function decorator to measure the execution time of Python functions. Includes code examples for beginners and advanced users.
tags:
    - Features
    - Tutorial
---

# How to Measure Time of Functions
When you want to measure the performance of a function, use the function decorator.

## What Is a Decorated Function?
The `@` preceding a function is called a decorator. Such decoractor wraps a function and gives extra functionality without changing the original function.

The pattern is:

```python title=""
@decorator
def function():
    # Function code
```

## Examples
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

!!! tip "How to Use Function and Arguments as Thread Name"
    If you want to keep track of the function and its arguments for troubleshooting, here's a tip on how to do it:

    ```python linenums="1" hl_lines="5 7"
    from timer import function_timer

    number = 1
    text = "some text"
    thread_name = f"test_function({number=}, {text=})"

    @function_timer(thread=thread_name)
    def test_function(number, text):
        # Insert your code here

    test_function(number, text)
    ```

    Terminal output example:

    ```text title=""
    Elapsed time (thread TEST_FUNCTION(NUMBER=1, TEXT='SOME TEXT')): 12.34 seconds
    ```

    Or if you don't know the arguments in advance, you can try a more dynamic approach:

    ```python linenums="1" hl_lines="8"
    from timer import function_timer

    def test_function(number, text):
        # Insert your code here

    arguments = (1, "some text")

    @function_timer(thread=f"{test_function.__name__}({', '.join(map(str, arguments))})")
    def wrapper(number, text):
        test_function(number, text)

    wrapper(*arguments)
    ```

    Terminal output example:

    ```text title=""
    Elapsed time (thread TEST_FUNCTION(1, SOME TEXT)): 12.34 seconds
    ```
