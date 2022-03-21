from colorist import Color

from .. import error
from ..constant.decimals import DEFAULT, MAXIMUM, MINIMUM
from ..model.timer_base import TimerBase


def mediate(timer: TimerBase, decimals: int | None) -> int:
    """If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated."""

    return timer.decimals if decimals is None else validate_and_normalise(decimals)


def validate_and_normalise(decimals: int | float | None) -> int:
    try:
        if not isinstance(decimals, (int, float)) or decimals is None:
            print(f"{Color.YELLOW}Timer: Decimals set to default {DEFAULT} due to invalid input.{Color.OFF}")
            return DEFAULT
        elif decimals > MAXIMUM:
            print(f"{Color.YELLOW}Timer: Decimals set to {MAXIMUM} as the Timer doesn't support more than {MAXIMUM} decimals (i.e. nanoseconds).{Color.OFF}")
            return MAXIMUM
        elif MINIMUM <= decimals <= MAXIMUM:
            if decimals % 1 == 0:
                return int(decimals)
            decimals_rounded = int(round(decimals))
            print(f"{Color.YELLOW}Timer: Decimals {decimals} set to {decimals_rounded} as a floating number is invalid input.{Color.OFF}")
            return decimals_rounded
        else:
            print(f"{Color.YELLOW}Timer: Decimals set to default {DEFAULT} due to invalid input.{Color.OFF}")
            return DEFAULT
    except Exception:
        error.message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")
        return DEFAULT
