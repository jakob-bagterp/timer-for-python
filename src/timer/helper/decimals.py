from .. import constants
from . import colour
from .. import error
from ..model.timer import TimerObject

def mediate(timer: TimerObject, decimals: int) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
    return timer.decimals if decimals is None else validate_and_normalise(decimals)

def validate_and_normalise(decimals: int) -> int:
    try:
        if isinstance(decimals, str) is True or decimals is None:
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
