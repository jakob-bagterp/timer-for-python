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
Use the `@function_timer()` as decorator to measure the performance of a function. Then the Timer will be triggered each time the function is called, and the clock will stop automatically when the function is finished:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer()
def test_function():
    # Insert your code here

test_function()
```

How it appears in the terminal:

<pre><code>% Elapsed time: 12.34 seconds for thread <span class="fg-green">TEST_FUNCTION</span></code></pre>

!!! tip "How to Get Function and Arguments as Thread Name"
    If you want to keep track of a [function and its arguments](https://www.w3schools.com/python/gloss_python_function_arguments.asp) for troubleshooting and measuring the performance of a function, it's already handled by the `@function_timer()` decorator. For example:

    ```python linenums="1" hl_lines="3-4"
    from timer import function_timer

    @function_timer()
    def sum_numbers(a, b):
        return a + b

    sum_numbers(1, 2)
    ```

    How it appears in the terminal:

    <pre><code>% Elapsed time: 0.12 seconds for thread <span class="fg-green">SUM_NUMBERS(A=1, B=2)</span></code></pre>

    This also works with [keyword arguments](https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp):

    ```python linenums="1" hl_lines="3-4"
    from timer import function_timer

    @function_timer()
    def anonymous_last_name(first_name, last_name = "unknown"):
        return f"{first_name} {last_name}"

    anonymous_last_name("John")
    ```

    How it appears in the terminal:

    <pre><code>% Elapsed time: 0.12 seconds for thread <span class="fg-green">ANONYMOUS_LAST_NAME(FIRST_NAME='JOHN', LAST_NAME='UNKNOWN')</span></code></pre>

### Custom Thread Name and Decimals
Similar to customising [output decimals](decimals.md) and [thread name](multiple-threads.md) for the Timer, this is also possible with the `@function_timer()` decorator. Simply use the `thread` and `decimals` arguments where the custom thread will override the default function name and list of arguments:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer(thread="custom", decimals=5)
def sum_numbers(a, b):
    return a + b

sum_numbers(1, 2)
```

How it appears in the terminal:

<pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">CUSTOM</span></code></pre>
