from _mock_data.thread_list import (THREAD_ITEM_A, THREAD_ITEM_B, THREAD_ITEM_C, THREAD_ITEM_DEFAULT,
                                    generate_threads_list)

import timer.constant as constant
import timer.helper.thread as thread
from timer import Timer


def test_try_get_thread_item_and_index() -> None:
    timer = Timer()
    assert len(timer._threads) == 0
    timer._threads = generate_threads_list()
    assert len(timer._threads) == 4
    assert THREAD_ITEM_DEFAULT, 0 == thread.list.try_get_thread_item_and_index(timer, constant.various.NONE_VALUE)
    assert THREAD_ITEM_A, 1 == thread.list.try_get_thread_item_and_index(timer, "A")
    assert THREAD_ITEM_B, 2 == thread.list.try_get_thread_item_and_index(timer, "B")
    assert THREAD_ITEM_C, 3 == thread.list.try_get_thread_item_and_index(timer, "C")
    del timer
