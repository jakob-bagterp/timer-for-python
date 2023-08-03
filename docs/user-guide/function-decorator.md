---
tags:
    - Features
    - Tutorial
---

# Function Decorator
## What Is a Decorated Function?
The `@` above a function is called a decorator. Such decoractor wraps the function below and gives extra functionality without changing the original function.

The pattern is:

```python title=""
@decorator
def some_function():
    # Function code
```

## Example
Use the `benchmark_timer` as function decorator:

```python linenums="1" hl_lines="3"
from timer import benchmark_timer

@benchmark_timer
def test_function():
    # Insert your code here

test_function()
```

Terminal output example:

```text title=""
Elapsed time: 12.34 seconds for thread TEST_FUNCTION
```
