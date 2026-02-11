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

    days = randint(0, 60)
    hours = randint(0, 24 - 1)
    minutes = randint(0, 60 - 1)
    seconds = randint(0, 60 - 1)
    milliseconds = randint(0, 1000 - 1)
    microseconds = randint(0, 1000 - 1)
    nanoseconds = randint(0, 1000 - 1)

    elapsed_time_ns = (
        days_as_ns(days)
        + hours_as_ns(hours)
        + minutes_as_ns(minutes)
        + seconds_as_ns(seconds)
        + milliseconds_as_ns(milliseconds)
        + microseconds_as_ns(microseconds)
        + nanoseconds
    )

    elapsed_time_fractions = ElapsedTimeFractions(
        nanoseconds, microseconds, milliseconds, seconds, minutes, hours, days
    )

    return elapsed_time_ns, elapsed_time_fractions


def mediate_zero(allow_zero: bool) -> int:
    return 0 if allow_zero else 1  # Used for ranges where you need at least 1 day, 1 hour, 1 minute, etc.


def random_nanoseconds_as_ns(allow_zero: bool = True) -> int:
    return randint(mediate_zero(allow_zero), 1000 - 1)


def random_microseconds_as_ns(allow_zero: bool = True) -> int:
    random_microseconds = randint(mediate_zero(allow_zero), 1000 - 1)
    return microseconds_as_ns(random_microseconds) + random_nanoseconds_as_ns()


def random_milliseconds_as_ns(allow_zero: bool = True) -> int:
    random_milliseconds = randint(mediate_zero(allow_zero), 1000 - 1)
    return milliseconds_as_ns(random_milliseconds) + random_microseconds_as_ns()


def random_seconds_as_ns(allow_zero: bool = True) -> int:
    random_seconds = randint(mediate_zero(allow_zero), 60 - 1)
    return seconds_as_ns(random_seconds) + random_milliseconds_as_ns()


def random_minutes_as_ns(allow_zero: bool = True) -> int:
    random_minutes = randint(mediate_zero(allow_zero), 60 - 1)
    return minutes_as_ns(random_minutes) + random_milliseconds_as_ns()


def random_hours_as_ns(allow_zero: bool = True) -> int:
    random_hours = randint(mediate_zero(allow_zero), 24 - 1)
    return hours_as_ns(random_hours) + random_minutes_as_ns()


def random_days_as_ns(allow_zero: bool = True) -> int:
    random_days = randint(mediate_zero(allow_zero), 60 - 1)
    return days_as_ns(random_days) + random_hours_as_ns()
