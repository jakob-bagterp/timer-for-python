import re
import time

from _helper.terminal_output import get_terminal_output_regex

from timer import Timer
from timer.constant.decimals import MAXIMUM, MINIMUM


def test_timer_decimals_output(capfd: object) -> None:
    for decimals in range(MINIMUM, MAXIMUM + 1):
        with Timer(decimals=decimals):
            time.sleep(0.001)
        terminal_output, _ = capfd.readouterr()
        expected_output_regex = get_terminal_output_regex(decimals=decimals)
        assert re.fullmatch(expected_output_regex, terminal_output)
