---
tags:
    - Features
---

# Humanised Output
## What Is Humanised Time?
Timer for Python supports measurement of time from nanoseconds to days.

But. If a program runs for a minute, it doesn't make sense to display the output time in 60,000 milliseconds. And similarly if it runs an hour, it doesn't make sense to display the output time in 3,600 seconds.

Therefore, the output of Timer is _humanised_ so it's easier to read.

## Examples
How different time ranges may appear in the terminal:

```text title=""
Elapsed time: 123 nanoseconds
Elapsed time: 4.56 microseconds
Elapsed time: 56.78 milliseconds
Elapsed time: 7.89 seconds
Elapsed time: 67.89 seconds (1m 8s)
Elapsed time: 3m 4s
Elapsed time: 2h 3m 4s
Elapsed time: 1d 2h 3m 4s
```
