from _mock_data.decimals import DECIMALS_RANGE

from timer import Timer
from timer.constant.decimals import DEFAULT
from timer.helper.decimals import mediate

# As decimals both can be set on the Timer object and the timer.start() function,
# let's ensure that decimals set in the timer.start() function takes precedence.
# NB: Always delete Timer object after each test since it's a singleton and we therefore want to avoid conflicts.


def test_mediate_of_start_timer_without_any_decimals_set_by_user() -> None:
    """Case: When the user initiates the Timer with default decimals and doesn't set any decimals when using "timer.start()", i.e. decimals should be default value."""

    timer = Timer()
    assert mediate(timer, None) == DEFAULT
    del timer


def test_mediate_of_start_timer_with_decimals_override_set_by_user() -> None:
    """Case: When the user initiates the Timer with default or custom decimals and wants to override this by using, e.g., "timer.start(decimals = 7)"."""

    for decimals_timer in DECIMALS_RANGE:
        timer = Timer(decimals_timer)
        for decimals_start in DECIMALS_RANGE:
            assert mediate(timer, decimals_start) == decimals_start
        del timer
