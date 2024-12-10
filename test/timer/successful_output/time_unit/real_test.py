import re
import time
from dataclasses import dataclass

import pytest
from _constant.time_unit import TimeUnit
from _helper import operating_system, python_version
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer import Timer

# TODO: Manipulate the Timer's start time to check output for nanoseconds and up days.


@dataclass(frozen=True, slots=True)
class TimeUnitTestSet:
    wait_seconds: float
    thread: str | None
    expected_time_unit: TimeUnit


SECONDS_TEST_SET_WITH_THREAD = TimeUnitTestSet(wait_seconds=1, expected_time_unit=TimeUnit.SECONDS, thread="custom")
SECONDS_TEST_SET_WITHOUT_THREAD = TimeUnitTestSet(wait_seconds=1, expected_time_unit=TimeUnit.SECONDS, thread=None)
MILLISECONDS_TEST_SET_WITH_THREAD = TimeUnitTestSet(wait_seconds=0.001, expected_time_unit=TimeUnit.MILLISECONDS, thread="custom")
MILLISECONDS_TEST_SET_WITHOUT_THREAD = TimeUnitTestSet(wait_seconds=0.001, expected_time_unit=TimeUnit.MILLISECONDS, thread=None)
MICROSECONDS_TEST_SET_WITH_THREAD = TimeUnitTestSet(wait_seconds=0.000_001, expected_time_unit=TimeUnit.MICROSECONDS, thread="custom")
MICROSECONDS_TEST_SET_WITHOUT_THREAD = TimeUnitTestSet(wait_seconds=0.000_001, expected_time_unit=TimeUnit.MICROSECONDS, thread=None)


@pytest.mark.parametrize("test_set", [
    SECONDS_TEST_SET_WITH_THREAD,
    SECONDS_TEST_SET_WITHOUT_THREAD,
    MILLISECONDS_TEST_SET_WITH_THREAD,
    MILLISECONDS_TEST_SET_WITHOUT_THREAD,
    MICROSECONDS_TEST_SET_WITH_THREAD,
    MICROSECONDS_TEST_SET_WITHOUT_THREAD,
])
def test_timer_time_unit_output(test_set: TimeUnitTestSet, capfd: object) -> None:
    if operating_system.is_windows() and python_version.is_3_10():
        pytest.skip("Skipping test for Python 3.10 on Windows since the sleep timer is flaky and inaccurate.")  # pragma: no cover
        return  # pragma: no cover

    ensure_all_timer_threads_are_stopped()
    with Timer():
        time.sleep(test_set.wait_seconds)

    terminal_output, _ = capfd.readouterr()
    expected_output_regex = successful_output_regex(time_unit=test_set.expected_time_unit)
    assert re.fullmatch(expected_output_regex, terminal_output)
