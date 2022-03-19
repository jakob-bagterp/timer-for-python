import time

import timer.constant as constant
from timer import Timer
from timer.model.thread_item import ThreadItem

THREAD_ITEM_DEFAULT: ThreadItem = ThreadItem(
    name=constant.various.NONE_VALUE,
    start_time=time.perf_counter_ns(),
    decimals=constant.decimals.DEFAULT
)

THREAD_ITEM_A: ThreadItem = ThreadItem(
    name="A",
    start_time=time.perf_counter_ns(),
    decimals=0
)

THREAD_ITEM_B: ThreadItem = ThreadItem(
    name="B",
    start_time=time.perf_counter_ns(),
    decimals=9
)

THREAD_ITEM_C: ThreadItem = ThreadItem(
    name="C",
    start_time=time.perf_counter_ns(),
    decimals=4
)

EMPTY_THREADS_LIST: list[ThreadItem] = []


def generate_threads_list() -> list[ThreadItem]:
    return [
        THREAD_ITEM_DEFAULT,
        THREAD_ITEM_A,
        THREAD_ITEM_B,
        THREAD_ITEM_C
    ]


def generate_timer_with_threads_list() -> Timer:
    timer = Timer()
    timer.threads = generate_threads_list()
    return timer
