__all__ = ["start_controller", "stop_controller", "message_for_action"]

import helper.thread

from constants import Constants
constants = Constants()

from text_colour import TextColour
colour = TextColour()

def start_controller(thread: str) -> None:
    if helper.thread.is_none(thread):
        print(f"{colour.yellow}Timer is running. Use .stop() to stop it.{colour.reset}")
    else:
        print(f"{colour.yellow}Timer for thread {thread} is running. Use .stop({thread = }) to stop it.{colour.reset}")

def stop_controller(timer: object, thread: str) -> None:
    if helper.thread.is_none(thread):
        print(f"{colour.yellow}Timer is not running. Use .start() to start it.{colour.reset}")
    else:
        print(f"{colour.yellow}Timer for thread {thread} is not running. Use .start({thread = }) to start it.{colour.reset}")
    if len(timer.thread_list) > 0:
        open_threads = [entry.get(constants.list_key.thread) for entry in timer.thread_list]
        print(f"Or maybe you aren't stopping the right thread? Currently open threads: {', '.join(open_threads)}")

def message_for_action(action: str, thread: str = None) -> None:
    print(f"{colour.yellow}Timer: Something went wrong {action}{'' if helper.thread.is_none(thread) else f' for thread {thread}'}.{colour.reset}")
