from ..model.elapsed_time_fractions import ElapsedTimeFractions

def calculate_time_fractions(elapsed_time_ns: int) -> ElapsedTimeFractions: # Elapsed time is in nanoseconds and should be calculated as difference between start and stop time using on the time.perf_counter_ns() function. 
	microseconds, nanoseconds = divmod(elapsed_time_ns, 1000)
	milliseconds, microseconds = divmod(microseconds, 1000) if microseconds > 0 else (0, 0) # As divmod() can be slow, let's return 0s as a tuple if divmod() isn't needed.
	seconds, milliseconds = divmod(milliseconds, 1000) if milliseconds > 0 else (0, 0)
	minutes, seconds = divmod(seconds, 60) if seconds > 0 else (0, 0)
	hours, minutes = divmod(minutes, 60) if minutes > 0 else (0, 0)
	days, hours = divmod(hours, 24) if hours > 0 else (0, 0)

	return ElapsedTimeFractions(
		nanoseconds = int(nanoseconds), 
		microseconds = int(microseconds),
		milliseconds = int(milliseconds),
		seconds = int(seconds),
		minutes = int(minutes),
		hours = int(hours),
		days = int(days))

class TimeFractions:
	def __init__(self, elapsed_time_ns: int) -> None:
		self.time: ElapsedTimeFractions = calculate_time_fractions(elapsed_time_ns)

	def count_microseconds_to_float(self) -> float:
		return self.time.microseconds + self.time.nanoseconds / 1000
		
	def count_milliseconds_to_float(self) -> float:
		return self.time.milliseconds + self.count_microseconds_to_float() / 1000 # This could potentially be faster by dividing self.microseconds by a 1000 directly, yet we don't want to lose precision in the decimals.

	def count_seconds_to_float(self) -> float:
		return self.time.seconds + self.count_milliseconds_to_float() / 1000 # This could potentially be faster by dividing self.milliseconds by a 1000 directly, yet we don't want to lose precision in the decimals.

	def seconds_rounded(self) -> float: # If 2 seconds and 567 milliseconds, ensure it'll be rounded up to 3 seconds.
		return int(round(self.count_seconds_to_float(), 0))

	def count_minutes_to_seconds(self) -> float:
		return self.time.minutes * 60 + self.count_seconds_to_float()
