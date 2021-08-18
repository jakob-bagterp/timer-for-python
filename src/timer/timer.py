import time
from time_fractions import TimeFractions
from text_colour import TextColour

textcolour = TextColour()

class Timer:
	_none_value = "NONE" # NB: Has to be string and upppercase.
	_list_key_thread = "thread"
	_list_key_start_time = "start_time"
	_list_key_decimals = "decimals"
	_decimals_default = 2

	def __init__(self, decimals: int = _decimals_default) -> None:
		self.thread_list = []
		self.decimals = decimals if decimals == self._decimals_default else self.verify_decimals(decimals)

	def start(self, thread: str = None, decimals: int = None) -> None:
		try:
			start_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			thread = self.normalise_thread_to_string_and_uppercase(thread)
			decimals = self.decimals_controller(decimals)
			self.thread_controller_start(thread, start_time, decimals)
		except Exception:
			self.print_error_message_for_action("when trying to start the Timer", thread = thread)

	def stop(self, thread: str = None) -> None:
		try:
			stop_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			thread = self.normalise_thread_to_string_and_uppercase(thread)
			self.thread_controller_stop(thread, stop_time)
		except Exception:
			self.print_error_message_for_action("when trying to stop the Timer", thread = thread)

	def output_message(self, thread: str, elapsed_time: int, decimals: int) -> None:
		try:
			text_intro = f"Elapsed time{'' if self.is_thread_none(thread) else f' (thread {textcolour.green}{thread}{textcolour.reset})'}:"
			fractions = TimeFractions(elapsed_time)
			if fractions.days > 0:
				print(f"{text_intro} {fractions.days}d {fractions.hours}h {fractions.minutes}m {fractions.seconds_rounded()}s") # Format: 1d 2h 3m 4s
			elif fractions.hours > 0:
				print(f"{text_intro} {fractions.hours}h {fractions.minutes}m {fractions.seconds_rounded()}s") # Format: 1h 2m 3s
			elif fractions.minutes > 0:
				print(f"{text_intro} {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({fractions.minutes}m {fractions.seconds_rounded()}s)") # Format: 62.34 seconds (1m 2s)
			elif fractions.seconds > 0:
				print(f"{text_intro} {fractions.count_seconds_to_float():.{decimals}f} seconds") # Format: 0.123456789 seconds
			elif fractions.milliseconds > 0:
				print(f"{text_intro} {fractions.count_milliseconds_to_float():.{decimals}f} milliseconds") # Format: 123.45 milliseconds
			elif fractions.microseconds > 0:
				print(f"{text_intro} {fractions.count_microseconds_to_float():.{decimals}f} microseconds") # Format: 234.56 microseconds
			else:
				print(f"{text_intro} {fractions.nanoseconds} nanoseconds") # Format: 345 nanoseconds
		except Exception:
			self.print_error_message_for_action(f"in the Timer's output message module", thread = thread)

	def decimals_controller(self, decimals: str) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
		return self.decimals if decimals == None else self.verify_decimals(decimals)

	def thread_controller_start(self, thread: str, start_time: int, decimals: int) -> None:
		try:
			entry_index = self.lookup_index_in_thread_list(thread)
			if entry_index == None: # If no match in existing threads, create new entry in the thread list.
				self.add_to_thread_list(thread, start_time, decimals)
			else:
				self.error_handling_of_start_controller(thread)
		except Exception:
			self.print_error_message_for_action(f"in the Timer's start thread controller", thread = thread)

	def error_handling_of_start_controller(self, thread: str) -> None:
		if self.is_thread_none(thread):
			print(f"{textcolour.yellow}Timer is running. Use .stop() to stop it.{textcolour.reset}")
		else:
			print(f"{textcolour.yellow}Timer for thread {thread} is running. Use .stop({thread = }) to stop it.{textcolour.reset}")

	def thread_controller_stop(self, thread: str, stop_time: int) -> None:
		try:
			entry_index = self.lookup_index_in_thread_list(thread)
			if entry_index != None: # If there's a match in existing threads, return values to the stop function and remove the entry.
				start_time, decimals = self.get_start_time_and_decimals_from_thread_list(entry_index)
				elapsed_time = stop_time - start_time
				self.remove_from_thread_list(entry_index)
				self.output_message(thread, elapsed_time, decimals)
			else:
				self.error_handling_of_stop_controller(thread)
		except Exception:
			self.print_error_message_for_action(f"in the Timer's stop thread controller", thread = thread)

	def error_handling_of_stop_controller(self, thread: str) -> None:
		if self.is_thread_none(thread):
			print(f"{textcolour.yellow}Timer is not running. Use .start() to start it.{textcolour.reset}")
		else:
			print(f"{textcolour.yellow}Timer for thread {thread} is not running. Use .start({thread = }) to start it.{textcolour.reset}")
		if len(self.thread_list) > 0:
			open_threads = [entry.get(self._list_key_thread) for entry in self.thread_list]
			print(f"Or maybe you aren't stopping the right thread? Currently open threads: {', '.join(open_threads)}")

	def normalise_thread_to_string_and_uppercase(self, thread: str) -> str: # The thread list iterator only supports strings and numbers and not None, hence the renaming to "NONE".
		return self._none_value if self.is_thread_none(thread) else str(thread).upper()

	def lookup_index_in_thread_list(self, thread: str) -> int:
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

	def get_start_time_and_decimals_from_thread_list(self, entry_index: int) -> tuple[int, int]:
		try:
			entry = self.thread_list[entry_index]
			start_time = entry.get(self._list_key_start_time)
			decimals = entry.get(self._list_key_decimals)
			return start_time, decimals
		except Exception:
			self.print_error_message_for_action(f"when trying to look up the Timer values for entry index \"{entry_index}\"")

	def add_to_thread_list(self, thread, start_time: int, decimals: int) -> None:
		try:
			self.thread_list.append({
				self._list_key_thread: thread,
				self._list_key_start_time: start_time,
				self._list_key_decimals: decimals
			})
		except Exception:
			self.print_error_message_for_action(f"when trying to add entry to the Timer's thread list", thread = thread)

	def remove_from_thread_list(self, entry_index: int) -> None:
		try:
			self.thread_list.pop(entry_index)
		except Exception:
			self.print_error_message_for_action(f"when trying to remove entry from the Timer's thread list for entry index \"{entry_index}\"")

	def verify_decimals(self, decimals: int) -> int:
		try:
			if isinstance(decimals, str) == True or decimals == None:
				print(f"{textcolour.yellow}Timer: Decimals set to default {self._decimals_default} due to invalid input.{textcolour.reset}")
				return self._decimals_default
			elif decimals > 9:
				print(f"{textcolour.yellow}Timer: Decimals set to 9 as the Timer doesn't support more than 9 decimals (i.e. nanoseconds).{textcolour.reset}")
				return 9
			elif decimals in range(0, 10):
				return int(decimals)
			else:
				print(f"{textcolour.yellow}Timer: Decimals set to default {self._decimals_default} due to invalid input.{textcolour.reset}")
				return self._decimals_default
		except Exception:
			self.print_error_message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")

	def is_thread_none(self, thread: str) -> bool:
		return True if thread == None or thread == self._none_value else False

	def print_error_message_for_action(self, action: str, thread: str = None) -> None:
		print(f"{textcolour.yellow}Timer: Something went wrong {action}{'' if self.is_thread_none(thread) else f' for thread {thread}'}.{textcolour.reset}")
