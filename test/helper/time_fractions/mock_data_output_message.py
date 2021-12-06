from random import randint
from timer.constants.decimals import maximum, minimum

def random_decimals(max: int = maximum()) -> int:
    return randint(minimum(), max if minimum() < max <= maximum() else maximum())
