import time

class _TextColour:
	def __init__(self):
		self.green = "\033[92m"
		self.yellow = "\033[93m"
		self.reset = "\033[0m"

textcolour = _TextColour()

class Timer:
	_none_value = "NONE"
	_list_key_thread = "thread"
	_list_key_start_time = "start_time"
	_list_key_decimals = "decimals"
	_decimals_default = 2

	def __init__(self, decimals = _decimals_default):
		self.thread_list = []
		self.decimals = decimals if decimals == self._decimals_default else self.verify_decimals(decimals)

	def start(self, thread = None, decimals = None):
		try:
			start_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			thread = self.normalise_thread_to_string_and_uppercase(thread)
			decimals = self.decimals_controller(decimals)
			self.thread_controller_start(thread, start_time, decimals)
		except Exception:
			self.print_error_message_for_action("when trying to start the Timer", thread = thread)

	def stop(self, thread = None):
		try:
			stop_time = time.perf_counter_ns() # 	For precision, this is the first operation of the function.
			thread = self.normalise_thread_to_string_and_uppercase(thread)
			self.thread_controller_stop(thread, stop_time)
		except Exception:
			self.print_error_message_for_action("when trying to stop the Timer", thread = thread)

	class _Fractions:
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
		
	def count_microseconds_to_float(self, fractions):
		return fractions.microseconds + fractions.nanoseconds / 1000
		
	def count_milliseconds_to_float(self, fractions):
		return fractions.milliseconds + self.count_microseconds_to_float(fractions) / 1000

	def count_seconds_to_float(self, fractions):
		return fractions.seconds + self.count_milliseconds_to_float(fractions) / 1000

	def output_message(self, thread, elapsed_time, decimals):
		try:
			fractions = self._Fractions(elapsed_time)
			text_intro = "Elapsed time:" if self.is_thread_none(thread) else f"Elapsed time (thread {textcolour.green}{thread}{textcolour.reset}):"
			if fractions.days > 0:
				print(f"{text_intro} {fractions.days}d {fractions.hours}h {fractions.minutes}m {fractions.seconds}s") # Format: 1d 2h 3m 4s
			elif fractions.hours > 0:
				print(f"{text_intro} {fractions.hours}h {fractions.minutes}m {fractions.seconds}s") # Format: 1h 2m 3s
			elif fractions.minutes > 0:
				print(f"{text_intro} {self.count_seconds_to_float(fractions):.{decimals}f} seconds ({fractions.minutes}m {fractions.seconds}s)") # Format: 1m 2s
			elif fractions.seconds > 0:
				print(f"{text_intro} {self.count_seconds_to_float(fractions):.{decimals}f} seconds") # Format: 0.123456789 seconds
			elif fractions.milliseconds > 0:
				print(f"{text_intro} {self.count_milliseconds_to_float(fractions):.{decimals}f} milliseconds") # Format: 123.45 milliseconds
			elif fractions.microseconds > 0:
				print(f"{text_intro} {self.count_microseconds_to_float(fractions):.{decimals}f} microseconds") # Format: 234.56 microseconds
			else:
				print(f"{text_intro} {fractions.nanoseconds} nanoseconds") # Format: 345.67 nanoseconds
		except Exception:
			self.print_error_message_for_action(f"in the Timer's output message module", thread = thread)

	def decimals_controller(self, decimals):
		if decimals == None:
			return self.decimals
		else:
			return self.verify_decimals(decimals)

	def thread_controller_start(self, thread, start_time, decimals):
		try:
			entry_index = self.lookup_index_in_thread_list(thread)
			if entry_index == None: # If no match in existing threads, create new entry in the thread list.
				self.add_to_thread_list(thread, start_time, decimals)
			else:
				if self.is_thread_none(thread):
					print(f"{textcolour.yellow}Timer is running. Use .stop() to stop it.{textcolour.reset}")
				else:
					print(f"{textcolour.yellow}Timer for thread {thread} is running. Use .stop(thread={thread}) to stop it.{textcolour.reset}")
		except Exception:
			self.print_error_message_for_action(f"in the Timer's start thread controller", thread = thread)

	def thread_controller_stop(self, thread, stop_time):
		try:
			entry_index = self.lookup_index_in_thread_list(thread)
			if entry_index != None: # If there's a match in existing threads, return values to the stop function and remove the entry.
				start_time, decimals = self.get_start_time_and_decimals_from_thread_list(entry_index)
				elapsed_time = stop_time - start_time
				self.remove_from_thread_list(entry_index)
				self.output_message(thread, elapsed_time, decimals)
			else:
				if self.is_thread_none(thread):
					print(f"{textcolour.yellow}Timer is not running. Use .start() to start it.{textcolour.reset}")
				else:
					print(f"{textcolour.yellow}Timer for thread {thread} is not running. Use .start(thread={thread}) to start it.{textcolour.reset}")
				if len(self.thread_list) > 0:
					open_threads = [entry.get(self._list_key_thread) for entry in self.thread_list]
					print(f"Or maybe you aren't stopping the right thread? Currently open threads: {', '.join(open_threads)}")
		except Exception:
			self.print_error_message_for_action(f"in the Timer's stop thread controller", thread = thread)

	def normalise_thread_to_string_and_uppercase(self, thread):
		try:
			if self.is_thread_none(thread):
				return str(self._none_value).upper() # The thread list iterator only supports strings and numbers and not None, hence the renaming.
			else:
				return str(thread).upper()
		except Exception:
			self.print_error_message_for_action(f"when trying to normalise the Timer's input", thread = thread)

	def lookup_index_in_thread_list(self, thread):
		try:
			entry_index = None
			entry_counter = 0
			for entry in self.thread_list:
				if entry.get(self._list_key_thread) == thread: # Check if thread already exists in list. Note that this expects a normalised thread (i.e. string and not None) and already in uppercase so it evaluates as intended.
					entry_index = entry_counter
					break # Make sure only the first match is returned, yet the main function is not designed to allow input of duplicates.
				else:
					entry_counter += 1
			return entry_index
		except Exception:
			self.print_error_message_for_action(f"in the Timer's lookup module", thread = thread)

	def get_start_time_and_decimals_from_thread_list(self, entry_index):
		try:
			entry = self.thread_list[entry_index]
			start_time = entry.get(self._list_key_start_time)
			decimals = entry.get(self._list_key_decimals)
			return start_time, decimals
		except Exception:
			self.print_error_message_for_action(f"when trying to look up the Timer values for entry index \"{entry_index}\"")

	def add_to_thread_list(self, thread, start_time, decimals):
		try:
			self.thread_list.append({
				self._list_key_thread: thread,
				self._list_key_start_time: start_time,
				self._list_key_decimals: decimals
			})
		except Exception:
			self.print_error_message_for_action(f"when trying to add entry to the Timer's thread list", thread = thread)

	def remove_from_thread_list(self, entry_index):
		try:
			self.thread_list.pop(entry_index)
		except Exception:
			self.print_error_message_for_action(f"when trying to remove entry from the Timer's thread list for entry index \"{entry_index}\"")

	def verify_decimals(self, decimals):
		try:
			if isinstance(decimals, str) == True or decimals == None:
				print(f"{textcolour.yellow}Timer: Decimals set to default {self._decimals_default} due to invalid input.{textcolour.reset}")
				return self._decimals_default
			elif decimals in range(1, 10):
				return int(decimals)
			elif decimals > 9:
				print(f"{textcolour.yellow}Timer: Decimals set to 9 as the Timer doesn't support more than 9 decimals (i.e. nanoseconds).{textcolour.reset}")
				return 9
			else:
				print(f"{textcolour.yellow}Timer: Decimals set to default {self._decimals_default} due to invalid input.{textcolour.reset}")
				return self._decimals_default
		except Exception:
			self.print_error_message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")

	def is_thread_none(self, thread):
		return True if thread == None or thread == self._none_value else False

	def print_error_message_for_action(self, action, thread = None):
		if self.is_thread_none(thread):
			print(f"{textcolour.yellow}Timer: Something went wrong {action}.{textcolour.reset}")
		else:
			print(f"{textcolour.yellow}Timer: Something went wrong {action} for thread {thread}.{textcolour.reset}")
