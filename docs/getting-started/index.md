---
title: Get Started with Measuring Time in 2 Easy Steps
description: Quick guide to installing and using Timer for Python, so you can run your first script within minutes. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Installation
    - PyPI
---

# Get Started in 2 Easy Steps 🚀
Ready to try the easy way to measure the time and performance of your Python code? Let's get started:

## 1. Install Timer for Python Package
Assuming that [Python](https://www.python.org/) is already installed, execute this command in the terminal to install the Timer package:

```shell title=""
pip install timer-for-python
```

Find more details and options in the [installation guide](installation.md).

## 2. First Script
You're now ready to go:

```python linenums="1" hl_lines="6"
from timer import Timer

timer = Timer()
timer.start()

# Insert your code here

timer.stop()
```

After `timer.stop()`, the elapsed time will be printed in your terminal. Example:

```text title=""
% Elapsed time: 12.34 seconds
```

## Next Steps
Find more usage examples and tutorials in the [user guide](../user-guide/index.md) section.

## Support the Project
If you have already downloaded and tried the package, perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
