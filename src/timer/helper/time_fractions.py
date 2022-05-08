from ..model.elapsed_time_fractions import ElapsedTimeFractions


def calculate_time_fractions(elapsed_time_ns: int) -> ElapsedTimeFractions:
    """Elapsed time is in nanoseconds and should be calculated as difference between start and stop time using on the time.perf_counter_ns() function."""

    microseconds, nanoseconds = divmod(elapsed_time_ns, 1000)
    # As divmod() can be slow, let's return 0s as a tuple if divmod() isn't needed:
    milliseconds, microseconds = divmod(microseconds, 1000) if microseconds > 0 else (0, 0)
    seconds, milliseconds = divmod(milliseconds, 1000) if milliseconds > 0 else (0, 0)
    minutes, seconds = divmod(seconds, 60) if seconds > 0 else (0, 0)
    hours, minutes = divmod(minutes, 60) if minutes > 0 else (0, 0)
    days, hours = divmod(hours, 24) if hours > 0 else (0, 0)

    return ElapsedTimeFractions(
        nanoseconds=int(nanoseconds),
        microseconds=int(microseconds),
        milliseconds=int(milliseconds),
        seconds=int(seconds),
        minutes=int(minutes),
        hours=int(hours),
        days=int(days))
