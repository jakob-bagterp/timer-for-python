import time

from _mock_data.thread_list import THREAD_ITEM_A, THREAD_ITEM_B, THREAD_ITEM_C

import timer.constant as constant
import timer.helper.thread as thread
from timer import Timer


def test_add_to_empty_threads_list() -> None:
    timer = Timer()
    assert len(timer.threads) == 0
    thread.list.add(
        timer=timer,
        thread=constant.various.NONE_VALUE,
        start_time=time.perf_counter_ns(),
        decimals=constant.decimals.DEFAULT
    )
    assert len(timer.threads) == 1
    thread.list.add(
        timer=timer,
        thread="TEST",
        start_time=time.perf_counter_ns(),
        decimals=constant.decimals.MAXIMUM
    )
    assert len(timer.threads) == 2
    del timer


def test_added_thread_item_matches_input() -> None:
    timer = Timer()
    assert len(timer.threads) == 0
    thread.list.add(
        timer=timer,
        thread=THREAD_ITEM_A.name,
        start_time=THREAD_ITEM_A.start_time,
        decimals=THREAD_ITEM_A.decimals
    )
    assert len(timer.threads) == 1
    assert timer.threads[0] == THREAD_ITEM_A
    assert timer.threads[0] != THREAD_ITEM_B
    assert timer.threads[0] != THREAD_ITEM_C
    del timer
