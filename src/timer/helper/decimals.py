from .. import constants
from . import colour
from .. import error
from ..model.timer import TimerObject

def mediate(timer: TimerObject, decimals: int) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
    return timer.decimals if decimals is None else validate_and_normalise(decimals)

def validate_and_normalise(decimals: int) -> int:
    try:
        if isinstance(decimals, (str, list, dict, tuple)) is True or decimals is None:
            print(f"{colour.yellow()}Timer: Decimals set to default {constants.decimals.default()} due to invalid input.{colour.reset()}")
            return constants.decimals.default()
        elif decimals > constants.decimals.maximum():
            print(f"{colour.yellow()}Timer: Decimals set to {constants.decimals.maximum()} as the Timer doesn't support more than {constants.decimals.maximum()} decimals (i.e. nanoseconds).{colour.reset()}")
            return constants.decimals.maximum()
        elif 0 <= decimals <= constants.decimals.maximum():
            if decimals % 1 != 0:
                decimals_rounded = int(round(decimals))
                print(f"{colour.yellow()}Timer: Decimals {decimals} set to {decimals_rounded} as a floating number is invalid input.{colour.reset()}")
                return decimals_rounded
            else:
                return int(decimals)
        else:
            print(f"{colour.yellow()}Timer: Decimals set to default {constants.decimals.default()} due to invalid input.{colour.reset()}")
            return constants.decimals.default()
    except Exception:
        error.message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")
