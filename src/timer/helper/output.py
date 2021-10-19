from .. import error
from . import colour
from .. import helper
from ..helper.time_fractions import TimeFractions

def message(thread: str, fractions: TimeFractions, decimals: int) -> None:
    try:
        text_intro = f"Elapsed time{'' if helper.thread.is_none(thread) else f' (thread {colour.green()}{thread}{colour.reset()})'}:"
        time = fractions.time
        if time.days > 0:
            print(f"{text_intro} {time.days}d {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s") # Format: 1d 2h 3m 4s
        elif time.hours > 0:
            print(f"{text_intro} {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s") # Format: 1h 2m 3s
        elif time.minutes > 0:
            print(f"{text_intro} {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({time.minutes}m {fractions.seconds_rounded()}s)") # Format: 62.34 seconds (1m 2s)
        elif time.seconds > 0:
            print(f"{text_intro} {fractions.count_seconds_to_float():.{decimals}f} seconds") # Format: 0.123456789 seconds
        elif time.milliseconds > 0:
            print(f"{text_intro} {fractions.count_milliseconds_to_float():.{decimals}f} milliseconds") # Format: 123.45 milliseconds
        elif time.microseconds > 0:
            print(f"{text_intro} {fractions.count_microseconds_to_float():.{decimals}f} microseconds") # Format: 234.56 microseconds
        else:
            print(f"{text_intro} {time.nanoseconds} nanoseconds") # Format: 345 nanoseconds
    except Exception:
        error.message_for_action(f"in the Timer's output message module", thread = thread)
