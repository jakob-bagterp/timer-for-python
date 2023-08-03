---
tags:
    - Features
---

# Humanised Output
Timer for Python supports time measurement from nanoseconds to days.

But. If the Timer runs for several minutes, it doesn't make sense to display the output time in milliseconds. And similarly if it runs for hours, it doesn't make sense to display the output time in seconds.

Therefore, the output is "humanised" so it's easier to read. Examples:

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
