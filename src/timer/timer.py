import time
import controller
import helper.thread
import helper.thread.list
import error
from time_fractions import TimeFractions

from constants import Constants
constants = Constants()

from text_colour import TextColour
colour = TextColour()

class Timer:
	def __init__(self, decimals: int = constants.decimals.default) -> None:
		self.thread_list = []
		self.decimals = decimals if decimals == constants.decimals.default else helper.verify_decimals(decimals)

	def start(self, thread: str = None, decimals: int = None) -> None:
		try:
			start_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			thread = helper.thread.normalise_to_string_and_uppercase(thread)
			decimals = controller.decimals(self, decimals)
			controller.start(self, thread, start_time, decimals)
		except Exception:
			error.message_for_action("when trying to start the Timer", thread = thread)

	def stop(self, thread: str = None) -> None:
		try:
			stop_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			thread = helper.thread.normalise_to_string_and_uppercase(thread)
			self.thread_controller_stop(thread, stop_time)
		except Exception:
			error.message_for_action("when trying to stop the Timer", thread = thread)

	def output_message(self, thread: str, elapsed_time: int, decimals: int) -> None:
		try:
			text_intro = f"Elapsed time{'' if helper.thread.is_none(thread) else f' (thread {colour.green}{thread}{colour.reset})'}:"
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
			error.message_for_action(f"in the Timer's output message module", thread = thread)

	def thread_controller_stop(self, thread: str, stop_time: int) -> None:
		try:
			entry_index = helper.thread.list.lookup_index(self, thread)
			if entry_index != None: # If there's a match in existing threads, return values to the stop function and remove the entry.
				start_time, decimals = helper.thread.list.get_start_time_and_decimals(self, entry_index)
				elapsed_time = stop_time - start_time
				helper.thread.list.remove(self, entry_index)
				self.output_message(thread, elapsed_time, decimals)
			else:
				self.error_handling_of_stop_controller(thread)
		except Exception:
			error.message_for_action(f"in the Timer's stop thread controller", thread = thread)

	def error_handling_of_stop_controller(self, thread: str) -> None:
		if helper.thread.is_none(thread):
			print(f"{colour.yellow}Timer is not running. Use .start() to start it.{colour.reset}")
		else:
			print(f"{colour.yellow}Timer for thread {thread} is not running. Use .start({thread = }) to start it.{colour.reset}")
		if len(self.thread_list) > 0:
			open_threads = [entry.get(constants.list_key.thread) for entry in self.thread_list]
			print(f"Or maybe you aren't stopping the right thread? Currently open threads: {', '.join(open_threads)}")
