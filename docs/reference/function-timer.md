---
title: Documentation for Function Decorator
description: Learn how to use the function decorator to measure the execution time of Python functions. Includes code examples for beginners and advanced users.
tags:
    - Documentation
    - Tutorial
---

# function_timer
## Function Decorator
How to use `@function_timer` as function decorator:

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
