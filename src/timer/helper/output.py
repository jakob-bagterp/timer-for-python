from colorist import Color

from .. import error, helper
from ..model.time_fractions import TimeFractions


def message(thread: str, fractions: TimeFractions, decimals: int) -> None:
    try:
        text_intro = f"Elapsed time{'' if helper.thread.is_none(thread) else f' (thread {Color.GREEN}{thread}{Color.OFF})'}:"
        time = fractions.time
        if time.days > 0:
            # Format: 1d 2h 3m 4s
            print(f"{text_intro} {time.days}d {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s")
        elif time.hours > 0:
            # Format: 1h 2m 3s
            print(f"{text_intro} {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s")
        elif time.minutes > 0:
            # Format: 62.34 seconds (1m 2s)
            print(f"{text_intro} {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({time.minutes}m {fractions.seconds_rounded()}s)")
        elif time.seconds > 0:
            # Format: 0.123456789 seconds
            print(f"{text_intro} {fractions.count_seconds_to_float():.{decimals}f} seconds")
        elif time.milliseconds > 0:
            # Format: 123.45 milliseconds
            print(f"{text_intro} {fractions.count_milliseconds_to_float():.{decimals}f} milliseconds")
        elif time.microseconds > 0:
            # Format: 234.56 microseconds
            print(f"{text_intro} {fractions.count_microseconds_to_float():.{decimals}f} microseconds")
        else:
            # Format: 345 nanoseconds
            print(f"{text_intro} {time.nanoseconds} nanoseconds")
    except Exception:
        error.message_for_action("in the Timer's output message module", thread)
