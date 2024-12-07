from random import choices, randint
from string import ascii_uppercase

from timer.constant.decimals import MAXIMUM, MINIMUM


def random_decimals(max: int = MAXIMUM) -> int:
    """Get a random number of decimals between the minimum 0 and maximum 9."""

    return randint(MINIMUM, max if MINIMUM < max <= MAXIMUM else MAXIMUM)


def random_thread_name(length: int = randint(1, 10)) -> str:
    """Get a random thread name with a given or random length."""

    return "".join(choices(ascii_uppercase, k=length))
