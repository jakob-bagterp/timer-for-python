from timer.model.timer_base import TimerBase


def set_start_time_back_in_time(timer: TimerBase, time_delta_ns: int, thread_index: int = 0) -> TimerBase:
    """Set the start time back in time with a given time delta in nanoseconds. Useful when setting delta from the start time to emulate the elapsed time."""

    timer._threads[thread_index].start_time -= time_delta_ns
    return timer
