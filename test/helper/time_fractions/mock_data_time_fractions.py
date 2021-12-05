from random import randint
from timer.model.elapsed_time_fractions import ElapsedTimeFractions

def microseconds_as_ns(microseconds: int) -> int:
    return microseconds * 1000

def milliseconds_as_ns(milliseconds: int) -> int:
    return milliseconds * 1000 * microseconds_as_ns(1)

def seconds_as_ns(seconds: int) -> int:
    return seconds * 1000 * milliseconds_as_ns(1)

def minutes_as_ns(minutes: int) -> int:
    return minutes * 60 * seconds_as_ns(1)

def hours_as_ns(hours: int) -> int:
    return hours * 60 * minutes_as_ns(1)

def days_as_ns(days: int) -> int:
    return days * 24 * hours_as_ns(1)

def random_elapsed_time_ns_and_fractions() -> tuple[int, ElapsedTimeFractions]:
    """Returns tuple of elapsed time in nanoseconds and a corresponding ElapsedTimeFractions object."""
    
    _days = randint(0, 60)
    _hours = randint(0, 24 - 1)
    _minutes = randint(0, 60 - 1)
    _seconds = randint(0, 60 - 1)
    _milliseconds = randint(0, 1000 - 1)
    _microseconds = randint(0, 1000 - 1)
    _nanoseconds = randint(0, 1000 - 1)
    
    elapsed_time_ns = days_as_ns(_days) + hours_as_ns(_hours) + minutes_as_ns(_minutes) + seconds_as_ns(_seconds) + milliseconds_as_ns(_milliseconds) + microseconds_as_ns(_microseconds) + _nanoseconds
    
    elapsed_time_fractions = ElapsedTimeFractions(
        _nanoseconds,
        _microseconds,
        _milliseconds,
        _seconds,
        _minutes,
        _hours,
        _days)

    return elapsed_time_ns, elapsed_time_fractions
