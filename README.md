# Timer for Python
Timer for Python makes it easy for beginners and experts to measure how much time it takes to run Python programs and gauge performance of multiple, smaller bits of code.

## Prerequisites
* Python 3.8 or higher
	* It may work on earlier versions, but hasn't been tested
* macOS
	* It may work on Windows or Linux, but hasn't been tested

## Getting Started
### Simple
Add the Timer to your imports:

```python
from timer import Timer
```

Wrap your code with the Timer function to measure performance of the executed code block:

```python
timer = Timer()
timer.start()

# Insert your code here

timer.stop() # Output example: 12.34 seconds
```

### Advanced and Multiple Threads
To measure time of multiple instances within the same code block, use the `thread` argument:

```python
timer = Timer()
timer.start(thread = "A")

# Insert your code here

	timer.start(thread = "B", decimals = 5)

	# Insert more code here

	timer.stop(thread = "B") # Output example: 1.23456 seconds

# Insert even more code here

timer.stop(thread = "A")  # Output example: 7.89 seconds
```

## Features
### Precision
Timer for Python uses the native `time.perf_counter_ns()` function for maximum resolution in nanoseconds.

### Decimals in Output
To set the number of decimals of the output (only if less than an hour), use the `decimals` argument.

Either, set the general precision of decimals when initiating the Timer:

```python
timer = Timer(decimals = 5)
timer.start()

# Insert your code here

timer.stop() # Output example: 0.12345 seconds
```

Or set the decimals when starting a new thread:

```python
timer.start(decimals = 9)

# Insert your code here

timer.stop() # Output example: 0.123456789 seconds
```

#### Default Decimals
Default value for `decimals` is 2. The supported range is minimum 1 and maximum 9.

### Humanised Output
Timer for Python supports time measurement from nanoseconds to days.

But. If the Timer runs for several minutes, it doesn't make sense to display display the output time in milliseconds. And similarly if it runs for hours, it doesn't make sense to display the output time in seconds.

Therefore the output is "humanised" so it's easier to read:

```
Elapsed time: 7.89 seconds
Elapsed time: 67.89 seconds (1m 8s)
Elapsed time: 3m 4s
Elapsed time: 2h 3m 4s
Elapsed time: 1d 2h 3m 4s
```

### Graceful Error Handling
Timer for Python is designed with several nested `try/catch` clauses so it handles exceptions gracefully and therefore shouldn't break your application while running. However, if you find a bug, please report it.

## Donate
TBC

## Contribute
TBC

## Report Bugs
TBC
