__all__ = ["colour", "time_fractions", "thread", "output_message", "verify_decimals"]

import constants.decimals
import error
import helper.colour as colour
import helper.thread
from helper.time_fractions import TimeFractions

def mediate_decimals(timer: object, decimals: int) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
    return timer.decimals if decimals == None else helper.verify_decimals(decimals)

def verify_decimals(decimals: int) -> int:
    try:
        if isinstance(decimals, str) == True or decimals == None:
            print(f"{colour.yellow()}Timer: Decimals set to default {constants.decimals.default()} due to invalid input.{colour.reset()}")
            return constants.decimals.default()
        elif decimals > 9:
            print(f"{colour.yellow()}Timer: Decimals set to 9 as the Timer doesn't support more than 9 decimals (i.e. nanoseconds).{colour.reset()}")
            return 9
        elif decimals in range(0, 10):
            return int(decimals)
        else:
            print(f"{colour.yellow()}Timer: Decimals set to default {constants.decimals.default()} due to invalid input.{colour.reset()}")
            return constants.decimals.default()
    except Exception:
        error.message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")

def output_message(thread: str, elapsed_time: int, decimals: int) -> None:
    try:
        text_intro = f"Elapsed time{'' if helper.thread.is_none(thread) else f' (thread {colour.green()}{thread}{colour.reset()})'}:"
        fractions = TimeFractions(elapsed_time)
        if fractions.days > 0:
            print(f"{text_intro} {fractions.days}d {fractions.hours}h {fractions.minutes}m {fractions.seconds_rounded()}s") # Format: 1d 2h 3m 4s
        elif fractions.hours > 0:
            print(f"{text_intro} {fractions.hours}h {fractions.minutes}m {fractions.seconds_rounded()}s") # Format: 1h 2m 3s
        elif fractions.minutes > 0:
            print(f"{text_intro} {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({fractions.minutes}m {fractions.seconds_rounded()}s)") # Format: 62.34 seconds (1m 2s)
        elif fractions.seconds > 0:
            print(f"{text_intro} {fractions.count_seconds_to_float():.{decimals}f} seconds") # Format: 0.123456789 seconds
        elif fractions.milliseconds > 0:
            print(f"{text_intro} {fractions.count_milliseconds_to_float():.{decimals}f} milliseconds") # Format: 123.45 milliseconds
        elif fractions.microseconds > 0:
            print(f"{text_intro} {fractions.count_microseconds_to_float():.{decimals}f} microseconds") # Format: 234.56 microseconds
        else:
            print(f"{text_intro} {fractions.nanoseconds} nanoseconds") # Format: 345 nanoseconds
    except Exception:
        error.message_for_action(f"in the Timer's output message module", thread = thread)
