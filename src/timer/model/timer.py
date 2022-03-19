import time

from .. import constant, controller, error, helper
from .thread_item import ThreadItem
from .timer_base import TimerBase


class Timer(TimerBase):
    _instance = None
    _lock_init = False

    def __new__(cls, thread: str | None = None, decimals: int = constant.decimals.DEFAULT) -> TimerBase:
        if not cls._instance:  # Singleton: Ensure there's only a single instance of Timer running.
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, thread: str | None = None, decimals: int = constant.decimals.DEFAULT) -> None:
        if not self._lock_init:  # Ensure that initialisation of the lists only runs the first time.
            self.threads: list[ThreadItem] = []
            self.context_manager_threads: list[str] = []
            self._lock_init = True
        self.decimals: int = decimals if decimals == constant.decimals.DEFAULT else helper.decimals.validate_and_normalise(
            decimals)
        self.context_manager_latest_thread: str = helper.thread.normalise_to_string_and_uppercase(thread)
        self.context_manager_latest_decimals: int = self.decimals

    def __enter__(self) -> TimerBase:
        self.context_manager_threads.append(self.context_manager_latest_thread)
        self.start(self.context_manager_latest_thread, self.context_manager_latest_decimals)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        last_context_manager_thread = self.context_manager_threads.pop()
        self.stop(last_context_manager_thread)

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
