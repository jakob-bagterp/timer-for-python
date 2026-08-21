import re
import time

import pytest
from _constant.interval import ONE_MILLISECOND_AS_SECOND
from _helper import operating_system, python_version
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer import Timer
from timer.constant.decimals import MAXIMUM, MINIMUM


@pytest.mark.skipif(operating_system.is_windows() and python_version.is_3_10(), reason="Skipping test for Python 3.10 on Windows since the sleep timer is flaky and inaccurate.")
def test_timer_decimals_output(capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    for decimals in range(MINIMUM, MAXIMUM + 1):
        with Timer(decimals=decimals):
            time.sleep(ONE_MILLISECOND_AS_SECOND)
        terminal_output, _ = capfd.readouterr()
        expected_output_regex = successful_output_regex(decimals=decimals)
        assert re.fullmatch(expected_output_regex, terminal_output)
