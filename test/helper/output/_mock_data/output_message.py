from random import choices, randint
from string import ascii_uppercase
from timer.constant.decimals import MAXIMUM, MINIMUM

def random_decimals(max: int = MAXIMUM) -> int:
    return randint(MINIMUM, max if MINIMUM < max <= MAXIMUM else MAXIMUM)

def random_thread_name(length: int = randint(1, 10)) -> str:
    return "".join(choices(ascii_uppercase, k = length)) 
