import re
import time

from _constant.interval import ONE_MILLISECOND_AS_SECOND
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer import Timer
from timer.constant.decimals import MAXIMUM, MINIMUM


def test_timer_decimals_output(capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    for decimals in range(MINIMUM, MAXIMUM + 1):
        with Timer(decimals=decimals):
            time.sleep(ONE_MILLISECOND_AS_SECOND)
        terminal_output, _ = capfd.readouterr()
        expected_output_regex = successful_output_regex(decimals=decimals)
        assert re.fullmatch(expected_output_regex, terminal_output)
