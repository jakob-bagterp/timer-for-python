import time
import timer.constants as constants
from timer.model.thread_item import ThreadItem

def thread_item_default() -> ThreadItem:
    return ThreadItem(
        name = constants.none_value(),
        start_time = time.perf_counter_ns(),
        decimals = constants.decimals.default())

def thread_item_a() -> ThreadItem:
    return ThreadItem(
        name = "A",
        start_time = time.perf_counter_ns(),
        decimals = 0)

def thread_item_b() -> ThreadItem:
    return ThreadItem(
        name = "B",
        start_time = time.perf_counter_ns(),
        decimals = 9)

def thread_item_c() -> ThreadItem:
    return ThreadItem(
        name = "C",
        start_time = time.perf_counter_ns(),
        decimals = 4)

def empty_threads_list() -> list[ThreadItem]:
    return []
