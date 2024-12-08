import re
import time

import pytest
from _helper.terminal_output import get_terminal_output_regex

from timer import Timer


@pytest.mark.parametrize("wait_seconds, expected_time_unit", [
    (1, "seconds"),
    (0.001, "milliseconds"),
    (0.000_001, "microseconds"),
])
def test_timer_time_unit_output(wait_seconds: float, expected_time_unit: str, capfd: object) -> None:
    with Timer():
        time.sleep(wait_seconds)

    terminal_output, _ = capfd.readouterr()
    expected_output_regex = get_terminal_output_regex(time_unit=expected_time_unit)
    assert re.fullmatch(expected_output_regex, terminal_output)
