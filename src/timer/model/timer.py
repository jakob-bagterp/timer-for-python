import time

from .. import constant, controller, error, helper
from .thread_item import ThreadItem
from .timer_base import TimerBase


class Timer(TimerBase):

    _instance = None

    def __new__(cls, thread: str | None = None, decimals: int = constant.decimals.DEFAULT):
        if not cls._instance:  # Singleton: Ensure there's only a single instance of Timer running.
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, thread: str | None = None, decimals: int = constant.decimals.DEFAULT) -> None:
        self.decimals: int = decimals if decimals == constant.decimals.DEFAULT else helper.decimals.validate_and_normalise(
            decimals)
        if thread is None:
            self.threads: list[ThreadItem] = []
        else:
            self.threads: list[ThreadItem] = [ThreadItem(
                name=helper.thread.normalise_to_string_and_uppercase(thread),
                start_time=time.perf_counter_ns(),
                decimals=self.decimals
            )]

    def __enter__(self, thread: str | None = None, decimals: int | None = None):
        return self.start(thread, decimals)

    def __exit__(self, exc_type, exc_value, traceback, thread: str | None = None):
        self.stop(thread)

    def start(self, thread: str | None = None, decimals: int | None = None) -> None:
        try:
            start_time = time.perf_counter_ns()  # For precision, this is the first operation of the function.
            controller.start(self, thread, start_time, decimals)
        except Exception:
            error.message_for_action("when trying to start the Timer", thread)

    def stop(self, thread: str | None = None) -> None:
        try:
            stop_time = time.perf_counter_ns()  # For precision, this is the first operation of the function.
            controller.stop(self, thread, stop_time)
        except Exception:
            error.message_for_action("when trying to stop the Timer", thread)
