__all__ = ["TimeFractions"]

class TimeFractions:
	def __init__(self, elapsed_time_ns) -> None: # elapsed_time_ns is in nanoseconds and should be calculated as difference between start and stop time using on the time.perf_counter_ns() function. 
		_microseconds, _nanoseconds = divmod(elapsed_time_ns, 1000)
		_milliseconds, _microseconds = divmod(_microseconds, 1000) if _microseconds > 0 else (0, 0) # As divmod() can be slow, let's return 0s as a tuple if divmod() isn't needed.
		_seconds, _milliseconds = divmod(_milliseconds, 1000) if _milliseconds > 0 else (0, 0)
		_minutes, _seconds = divmod(_seconds, 60) if _seconds > 0 else (0, 0)
		_hours, _minutes = divmod(_minutes, 60) if _minutes > 0 else (0, 0)
		_days, _hours = divmod(_hours, 24) if _hours > 0 else (0, 0)
		self.nanoseconds = int(_nanoseconds)
		self.microseconds = int(_microseconds)
		self.milliseconds = int(_milliseconds)
		self.seconds = int(_seconds)
		self.minutes = int(_minutes)
		self.hours = int(_hours)
		self.days = int(_days)

	def count_microseconds_to_float(self) -> float:
		return self.microseconds + self.nanoseconds / 1000
		
	def count_milliseconds_to_float(self) -> float:
		return self.milliseconds + self.count_microseconds_to_float() / 1000 # This could potentially be faster by dividing self.microseconds by a 1000 directly, yet we don't want to lose precision in the decimals.

	def count_seconds_to_float(self) -> float:
		return self.seconds + self.count_milliseconds_to_float() / 1000 # This could potentially be faster by dividing self.milliseconds by a 1000 directly, yet we don't want to lose precision in the decimals.

	def seconds_rounded(self) -> float: # If 2 seconds and 567 milliseconds, ensure it'll be rounded up to 3 seconds.
		return int(round(self.count_seconds_to_float(), 0))

	def count_minutes_to_seconds(self) -> float:
		return self.minutes * 60 + self.count_seconds_to_float()
