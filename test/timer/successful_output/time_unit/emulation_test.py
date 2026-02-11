import re
from copy import deepcopy
from dataclasses import dataclass

import pytest
from _constant.time_unit import TimeUnit
from _helper.terminal_output import successful_output_regex
from _helper.thread_item import set_start_time_back_in_time
from _helper.time_fractions import (
    days_as_ns,
    hours_as_ns,
    microseconds_as_ns,
    milliseconds_as_ns,
    minutes_as_ns,
    seconds_as_ns,
)
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer import Timer


@dataclass(slots=True)
class TimeUnitEmulationTestSet:
    time_delta_ns: int
    expected_time_unit: TimeUnit
    thread: str | None
    decimals: int = 2


NANOSECONDS_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=-1_000_000, expected_time_unit=TimeUnit.NANOSECONDS, thread="custom"
)
NANOSECONDS_TEST_SET_WITHOUT_THREAD = deepcopy(NANOSECONDS_TEST_SET_WITH_THREAD)
NANOSECONDS_TEST_SET_WITHOUT_THREAD.thread = None

MICROSECONDS_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=microseconds_as_ns(123), expected_time_unit=TimeUnit.MICROSECONDS, thread="custom"
)
MICROSECONDS_TEST_SET_WITHOUT_THREAD = deepcopy(MICROSECONDS_TEST_SET_WITH_THREAD)
MICROSECONDS_TEST_SET_WITHOUT_THREAD.thread = None

MILLISECONDS_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=milliseconds_as_ns(123), expected_time_unit=TimeUnit.MILLISECONDS, thread="custom"
)
MILLISECONDS_TEST_SET_WITHOUT_THREAD = deepcopy(MILLISECONDS_TEST_SET_WITH_THREAD)
MILLISECONDS_TEST_SET_WITHOUT_THREAD.thread = None

SECONDS_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=seconds_as_ns(30), expected_time_unit=TimeUnit.SECONDS, thread="custom"
)
SECONDS_TEST_SET_WITHOUT_THREAD = deepcopy(SECONDS_TEST_SET_WITH_THREAD)
SECONDS_TEST_SET_WITHOUT_THREAD.thread = None

MINUTES_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=minutes_as_ns(10), expected_time_unit=TimeUnit.MINUTES, thread="custom"
)
MINUTES_TEST_SET_WITHOUT_THREAD = deepcopy(MINUTES_TEST_SET_WITH_THREAD)
MINUTES_TEST_SET_WITHOUT_THREAD.thread = None

HOURS_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=hours_as_ns(3), expected_time_unit=TimeUnit.HOURS, thread="custom"
)
HOURS_TEST_SET_WITHOUT_THREAD = deepcopy(HOURS_TEST_SET_WITH_THREAD)
HOURS_TEST_SET_WITHOUT_THREAD.thread = None

DAYS_TEST_SET_WITH_THREAD = TimeUnitEmulationTestSet(
    time_delta_ns=days_as_ns(2) + hours_as_ns(1) + minutes_as_ns(30) + seconds_as_ns(15),
    expected_time_unit=TimeUnit.DAYS,
    thread="custom",
)
DAYS_TEST_SET_WITHOUT_THREAD = deepcopy(DAYS_TEST_SET_WITH_THREAD)
DAYS_TEST_SET_WITHOUT_THREAD.thread = None


@pytest.mark.parametrize(
    "test_set",
    [
        NANOSECONDS_TEST_SET_WITH_THREAD,
        NANOSECONDS_TEST_SET_WITHOUT_THREAD,
        MICROSECONDS_TEST_SET_WITH_THREAD,
        MICROSECONDS_TEST_SET_WITHOUT_THREAD,
        MILLISECONDS_TEST_SET_WITH_THREAD,
        MILLISECONDS_TEST_SET_WITHOUT_THREAD,
        SECONDS_TEST_SET_WITH_THREAD,
        SECONDS_TEST_SET_WITHOUT_THREAD,
        MINUTES_TEST_SET_WITH_THREAD,
        MINUTES_TEST_SET_WITHOUT_THREAD,
        HOURS_TEST_SET_WITH_THREAD,
        HOURS_TEST_SET_WITHOUT_THREAD,
        DAYS_TEST_SET_WITH_THREAD,
        DAYS_TEST_SET_WITHOUT_THREAD,
    ],
)
def test_timer_emulated_time_unit_output(test_set: TimeUnitEmulationTestSet, capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    with Timer(thread=test_set.thread) as timer:
        timer = set_start_time_back_in_time(timer, test_set.time_delta_ns)

    terminal_output, _ = capfd.readouterr()
    expected_output_regex = successful_output_regex(
        thread=test_set.thread, decimals=test_set.decimals, time_unit=test_set.expected_time_unit
    )
    assert re.fullmatch(expected_output_regex, terminal_output)
