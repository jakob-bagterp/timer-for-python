from ..constant.decimals import DEFAULT, MAXIMUM, MINIMUM
from .colour import Colour
from .. import error
from ..model.timer import TimerObject

def mediate(timer: TimerObject, decimals: int | None) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
    return timer.decimals if decimals is None else validate_and_normalise(decimals)

def validate_and_normalise(decimals: int | None) -> int:
    try:
        if isinstance(decimals, (str, list, dict, tuple)) is True or decimals is None:
            print(f"{Colour.YELLOW}Timer: Decimals set to default {DEFAULT} due to invalid input.{Colour.RESET}")
            return DEFAULT
        elif decimals > MAXIMUM:
            print(f"{Colour.YELLOW}Timer: Decimals set to {MAXIMUM} as the Timer doesn't support more than {MAXIMUM} decimals (i.e. nanoseconds).{Colour.RESET}")
            return MAXIMUM
        elif MINIMUM <= decimals <= MAXIMUM:
            if decimals % 1 == 0:
                return int(decimals)
            decimals_rounded = int(round(decimals))
            print(f"{Colour.YELLOW}Timer: Decimals {decimals} set to {decimals_rounded} as a floating number is invalid input.{Colour.RESET}")
            return decimals_rounded
        else:
            print(f"{Colour.YELLOW}Timer: Decimals set to default {DEFAULT} due to invalid input.{Colour.RESET}")
            return DEFAULT
    except Exception:
        error.message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")
        return DEFAULT
