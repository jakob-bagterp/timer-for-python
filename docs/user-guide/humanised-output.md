---
title: Measure Time with Humanised Output
description: Learn how Timer for Python automatically converts and displays time measurements in human-readable format, from nanoseconds to days.
tags:
    - Features
---

# What Is Humanised Time?
Timer for Python supports measurement of time from nanoseconds to days.

But. If a program runs for a minute, it doesn't make sense to display the output time in 60,000 milliseconds. And similarly if it runs an hour, it doesn't make sense to display the output time in 3,600 seconds.

Therefore, the output of Timer is automatically _humanised_ so it's easier to read.

!!! info "How It Impacts the Decimals Configuration"
    While you can measure time from nanoseconds to seconds with [up to 9 decimals of a floating point number](decimals.md) by using `Timer(decimals=9)`, it doesn't always make sense. That's why the decimal configuration is overridden by humanised output in certain cases.

## Examples and Ranges
How different time ranges may appear in the terminal from fractions of a second to minutes, hours, days:

| Range                         | Decimals         | Terminal Output                                                                                                                                  |
| ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Nanoseconds                   | No decimals      | `Elapsed time: 123 nanoseconds`                                                                                                                  |
| From microseconds to seconds  | Up to 9 decimals | `Elapsed time: 4.56 microseconds`<br>`Elapsed time: 56.78 milliseconds`<br>`Elapsed time: 7.89 seconds`<br>`Elapsed time: 67.89 seconds (1m 8s)` |
| From minutes to days          | No decimals      | `Elapsed time: 3m 4s`<br>`Elapsed time: 2h 3m 4s`<br>`Elapsed time: 1d 2h 3m 4s`                                                                 |
