---
title: The Easy Way to Start, Stop and Measure Time
description: Timer for Python is a lightweight package that measures performance of your code. Get started in minutes with code examples for beginners and advanced users.
tags:
    - Tutorial
---

[![Latest version](https://img.shields.io/static/v1?label=version&message=0.9.6&color=yellowgreen)](https://github.com/jakob-bagterp/timer-for-python/releases/latest)
[![Python 3.10 | 3.11 | 3.12 | 3.13 | 3.14+](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%20|%203.12%20|%203.13%20|%203.14%2B&color=blueviolet)](https://www.python.org)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/timer-for-python/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/timer-for-python/branch/master/graph/badge.svg?token=P4IT8WQO0R)](https://codecov.io/gh/jakob-bagterp/timer-for-python)
[![CodeQL](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/github-code-scanning/codeql)
[![Test](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/timer-for-python/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/timer-for-python)](https://pepy.tech/project/timer-for-python)

# Timer for Python ⏳
## Why Use a Timer?
Measuring time and performance should be easy. If you want to measure the time it takes to run Python programs and measure the performance of multiple blocks of code, Timer for Python is a lightweight package that does the job.

## How It Works
### Basic Usage
Simply wrap the Timer around a block of code that you want to measure:

```python linenums="1" hl_lines="6"
from timer import Timer

timer = Timer()
timer.start()

# Insert your code here

timer.stop()
```

After `timer.stop()`, the elapsed time will be printed in the terminal:

```text title=""
% Elapsed time: 12.34 seconds
```

### Context Manager
Alternatively, use the `with` statement. This will [automatically start and stop the clock](user-guide/context-manager.md) – and so no need to declare `timer.start()` and `timer.stop()`. Same result as before, but less code:

```python linenums="1" hl_lines="4"
from timer import Timer

with Timer():
    # Insert your code here
```

How it appears in the terminal:

```text title=""
% Elapsed time: 12.34 seconds
```

### Multiple Threads
Gain total flexibility to measure the performance of different blocks of code using [multiple threads](user-guide/multiple-threads.md):

```python linenums="1" hl_lines="3 6"
from timer import Timer

with Timer(thread="A")
    # Insert your code here

    with Timer(thread="B", decimals=5):
        # Insert more code here

    # Insert even more code here
```

How it appears in the terminal:

<pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">B</span>
% Elapsed time: 6.78 seconds for thread <span class="fg-green">A</span></code></pre>

### Function Decorator
Or use `@function_timer()` as [function decorator](user-guide/function-decorator.md) to measure the performance of a function:

```python linenums="1" hl_lines="3"
from timer import function_timer

@function_timer()
def test_function():
    # Insert your code here

test_function()
```

How it appears in the terminal:

<pre><code>% Elapsed time: 12.34 seconds for thread <span class="fg-green">TEST_FUNCTION</span></code></pre>

## Next Steps
Ready to try? [Let's get started](getting-started/index.md).

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution makes a difference, whether you buy a coffee or support with a monthly donation. Find your tier here:

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
