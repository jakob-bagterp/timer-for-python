from timer import Timer
from timer.model.timer_base import TimerBase


def ensure_all_timer_threads_are_stopped() -> TimerBase:
    """Ensures all threads are stopped."""

    timer = Timer()
    timer._threads = []
    return timer


def get_timer_with_invalid_thread_type(thread: str) -> TimerBase:
    """Get a Timer with an invalid thread type. Instead of the the expected list[ThreadItem] type, adding a string will trigger an issue."""

    timer = ensure_all_timer_threads_are_stopped()
    timer._threads = [thread]
    return timer
