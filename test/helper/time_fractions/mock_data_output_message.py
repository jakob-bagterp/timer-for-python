from random import randint
from timer.constants.decimals import maximum, minimum

def random_decimals() -> int:
    return randint(minimum(), maximum())
