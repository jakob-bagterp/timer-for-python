__all__ = ["decimals", "start", "stop"]

import error
import helper
import helper.thread.list

def decimals(timer: object, decimals: int) -> int: # If the start function doesn't have decimals defined, then use the decimals value defined when the Timer() was initiated.
    return timer.decimals if decimals == None else helper.verify_decimals(decimals)

def start(timer: object, thread: str, start_time: int, decimals: int) -> None:
    try:
        entry_index = helper.thread.list.lookup_index(timer, thread)
        if entry_index == None: # If no match in existing threads, create new entry in the thread list.
            helper.thread.list.add(timer, thread, start_time, decimals)
        else:
            error.start_controller(thread)
    except Exception:
        error.message_for_action(f"in the Timer's start thread controller", thread = thread)

def stop(timer: object, thread: str, stop_time: int) -> None:
    try:
        entry_index = helper.thread.list.lookup_index(timer, thread)
        if entry_index != None: # If there's a match in existing threads, return values to the stop function and remove the entry.
            start_time, decimals = helper.thread.list.get_start_time_and_decimals(timer, entry_index)
            elapsed_time = stop_time - start_time
            helper.thread.list.remove(timer, entry_index)
            helper.output_message(thread, elapsed_time, decimals)
        else:
            error.stop_controller(timer, thread)
    except Exception:
        error.message_for_action(f"in the Timer's stop thread controller", thread = thread)
