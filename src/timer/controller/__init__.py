__all__ = ["decimals"]

import helper

def decimals(timer: object, decimals: int) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
    return timer.decimals if decimals == None else helper.verify_decimals(decimals)
