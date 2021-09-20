__all__ = ["verify_decimals", "thread"]

import error

from constants import Constants
constants = Constants()

from text_colour import TextColour
colour = TextColour()

def verify_decimals(decimals: int) -> int:
    try:
        if isinstance(decimals, str) == True or decimals == None:
            print(f"{colour.yellow}Timer: Decimals set to default {constants.decimals.default} due to invalid input.{colour.reset}")
            return constants.decimals.default
        elif decimals > 9:
            print(f"{colour.yellow}Timer: Decimals set to 9 as the Timer doesn't support more than 9 decimals (i.e. nanoseconds).{colour.reset}")
            return 9
        elif decimals in range(0, 10):
            return int(decimals)
        else:
            print(f"{colour.yellow}Timer: Decimals set to default {constants.decimals.default} due to invalid input.{colour.reset}")
            return constants.decimals.default
    except Exception:
        error.message_for_action(f"when trying to verify the Timer's decimals input \"{decimals}\"")
