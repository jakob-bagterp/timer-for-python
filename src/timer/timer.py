import time
import controller
import helper.thread
import error

from constants import Constants
constants = Constants()

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
			controller.stop(self, thread, stop_time)
		except Exception:
			error.message_for_action("when trying to stop the Timer", thread = thread)
