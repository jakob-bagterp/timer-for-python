import re
import time
from dataclasses import dataclass

import pytest
from _helper import operating_system, python_version
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer import Timer

# TODO: Manipulate the Timer's start time to check output for nanoseconds and up days.


@dataclass(frozen=True, slots=True)
class TimeUnitTestSet:
    wait_seconds: float
    expected_time_unit: str


SECONDS_TEST_SET = TimeUnitTestSet(wait_seconds=1, expected_time_unit="seconds")
MILLISECONDS_TEST_SET = TimeUnitTestSet(wait_seconds=0.001, expected_time_unit="milliseconds")
MICROSECONDS_TEST_SET = TimeUnitTestSet(wait_seconds=0.000_001, expected_time_unit="microseconds")


@pytest.mark.parametrize("test_set", [
    SECONDS_TEST_SET,
    MILLISECONDS_TEST_SET,
    MICROSECONDS_TEST_SET,
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


@pytest.mark.parametrize("test_set, thread", [
    (SECONDS_TEST_SET, "custom"),
    (MILLISECONDS_TEST_SET, "custom"),
    (MICROSECONDS_TEST_SET, "custom"),
])
def test_timer_time_unit_output_with_thread(test_set: TimeUnitTestSet, thread: str, capfd: object) -> None:
    if operating_system.is_windows() and python_version.is_3_10():
        pytest.skip("Skipping test for Python 3.10 on Windows since the sleep timer is flaky and inaccurate.")  # pragma: no cover
        return  # pragma: no cover

    ensure_all_timer_threads_are_stopped()
    with Timer(thread=thread):
        time.sleep(test_set.wait_seconds)

    terminal_output, _ = capfd.readouterr()
    expected_output_regex = successful_output_regex(thread=thread, time_unit=test_set.expected_time_unit)
    assert re.fullmatch(expected_output_regex, terminal_output)
