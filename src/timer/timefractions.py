class TimeFractions:
	def __init__(self, elapsed_time):
		_microseconds, _nanoseconds = divmod(elapsed_time, 1000)
		_milliseconds, _microseconds = divmod(_microseconds, 1000) if _microseconds > 0 else (0, 0)
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

	def count_microseconds_to_float(self):
		return self.microseconds + self.nanoseconds / 1000
		
	def count_milliseconds_to_float(self):
		return self.milliseconds + self.count_microseconds_to_float() / 1000

	def count_seconds_to_float(self):
		return self.seconds + self.count_milliseconds_to_float() / 1000

	def seconds_rounded(self): # If 2 seconds and 567 milliseconds, ensure it'll be rounded up to 3 seconds.
		return round(self.count_seconds_to_float(), 0)
