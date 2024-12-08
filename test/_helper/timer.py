from timer import Timer
from timer.model.timer_base import TimerBase


def ensure_all_timer_threads_are_stopped() -> TimerBase:
    """Ensures all threads are stopped."""

    timer = Timer()
    timer._threads = []
    return timer
