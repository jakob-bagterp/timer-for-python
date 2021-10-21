import time
from . import constants
from . import controller
from . import error
from . import helper
from .model.thread_item import ThreadItem
from .model.timer import TimerObject

class Timer(TimerObject):
	_instance = None

	def __new__(cls, *args, **kwargs) -> TimerObject:
		if not cls._instance: # Singleton: Ensure there's only a single instance of Timer running.
			cls._instance = TimerObject.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self, decimals: int = constants.decimals.default()) -> None:
		self.threads: list[ThreadItem] = []
		self.decimals: int = decimals if decimals == constants.decimals.default() else helper.decimals.validate_and_normalise(decimals)

	def start(self, thread: str = None, decimals: int = None) -> None:
		try:
			start_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			controller.start(self, thread, start_time, decimals)
		except Exception:
			error.message_for_action("when trying to start the Timer", thread = thread)

	def stop(self, thread: str = None) -> None:
		try:
			stop_time = time.perf_counter_ns() # For precision, this is the first operation of the function.
			controller.stop(self, thread, stop_time)
		except Exception:
			error.message_for_action("when trying to stop the Timer", thread = thread)
