from _helper.timer import ensure_all_timer_threads_are_stopped
from colorist import Color

from timer.constant.decimals import MAXIMUM, MINIMUM


def test_timer_decimals_below_accepted_value(capfd: object) -> None:
    timer = ensure_all_timer_threads_are_stopped()
    timer.start(decimals=MINIMUM - 1)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer: Decimals set to default 2 due to invalid input.{Color.OFF}\n"


def test_timer_decimals_above_accepted_value(capfd: object) -> None:
    timer = ensure_all_timer_threads_are_stopped()
    timer.start(decimals=MAXIMUM + 1)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer: Decimals set to 9 as the Timer doesn't support more than 9 decimals (i.e. nanoseconds).{Color.OFF}\n"
