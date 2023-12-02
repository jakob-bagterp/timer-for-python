---
title: Home
---

[![Latest version](https://img.shields.io/static/v1?label=version&message=0.7.1&color=yellowgreen)](https://github.com/jakob-bagterp/timer-for-python/releases/latest)
[![Python 3.10 | 3.11 or higher](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%2B&color=blueviolet)](https://www.python.org)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/timer-for-python/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/timer-for-python/branch/master/graph/badge.svg?token=P4IT8WQO0R)](https://codecov.io/gh/jakob-bagterp/timer-for-python)
[![CodeQL](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/timer-for-python)](https://pepy.tech/project/timer-for-python)

# Timer for Python ⏳
## Introduction
Performance timing made easy. When you want to measure how much time it takes to run Python programs and gauge performance of multiple blocks of code, Timer for Python is a lightweight Python package that gets the job done.

## How It Works
### Basics
Simply wrap the Timer around a block of code that you want to measure:

```python linenums="1" hl_lines="6"
from timer import Timer

timer = Timer()
timer.start()

# Insert your code here

timer.stop()
```

After `timer.stop()`, the elapsed time will be printed in your terminal. Example:

```text title=""
Elapsed time: 12.34 seconds
```

### Context Manager
Alternatively, use the `with` statement. This will automatically start and stop the Timer – and so no need to declare `timer.start()` and `timer.stop()`. Same result as before, but less code:

```python linenums="1" hl_lines="4"
from timer import Timer

with Timer():
    # Insert your code here
```

Terminal output example:

```text title=""
Elapsed time: 12.34 seconds
```

### Function Decorator
Or use `@benchmark_timer` as function decorator:

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

Ready to try? [Let's get started](./getting-started/index.md).
