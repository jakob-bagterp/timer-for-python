from random import choices, randint
from string import ascii_uppercase
from timer.constants.decimals import maximum, minimum

def random_decimals(max: int = maximum()) -> int:
    return randint(minimum(), max if minimum() < max <= maximum() else maximum())

def random_thread_name(length: int = randint(1, 10)) -> str:
    return "".join(choices(ascii_uppercase, k = length)) 
