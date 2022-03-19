from _mock_data.thread_list import (THREAD_ITEM_A, THREAD_ITEM_B,
                                    THREAD_ITEM_C, THREAD_ITEM_DEFAULT,
                                    generate_timer_with_threads_list)

import timer.helper.thread as thread
from timer import Timer


def test_remove_items_from_threads_list() -> None:
    timer = generate_timer_with_threads_list()
    assert len(timer.threads) == 4
    thread.list.remove(timer, 0)
    assert len(timer.threads) == 3
    thread.list.remove(timer, 2)
    assert len(timer.threads) == 2
    thread.list.remove(timer, 1)
    assert len(timer.threads) == 1
    thread.list.remove(timer, 0)
    assert len(timer.threads) == 0
    del timer


def test_removed_item_from_threads_list_matches_remaining_items() -> None:
    timer = Timer()
    assert len(timer.threads) == 0
    timer.threads = [
        THREAD_ITEM_DEFAULT,
        THREAD_ITEM_A,
        THREAD_ITEM_B,
        THREAD_ITEM_C
    ]
    assert len(timer.threads) == 4
    assert timer.threads[0] == THREAD_ITEM_DEFAULT
    assert timer.threads[1] == THREAD_ITEM_A
    assert timer.threads[2] == THREAD_ITEM_B
    assert timer.threads[3] == THREAD_ITEM_C
    thread.list.remove(timer, 0)
    assert len(timer.threads) == 3
    assert timer.threads[0] == THREAD_ITEM_A
    assert timer.threads[1] == THREAD_ITEM_B
    assert timer.threads[2] == THREAD_ITEM_C
    thread.list.remove(timer, 1)
    assert len(timer.threads) == 2
    assert timer.threads[0] == THREAD_ITEM_A
    assert timer.threads[1] == THREAD_ITEM_C
    thread.list.remove(timer, 0)
    assert len(timer.threads) == 1
    assert timer.threads[0] == THREAD_ITEM_C
    thread.list.remove(timer, 0)
    assert not timer.threads
    del timer
