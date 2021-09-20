__all__ = ["start_controller", "message_for_action"]

import helper.thread

from text_colour import TextColour
colour = TextColour()

def start_controller(thread: str) -> None:
    if helper.thread.is_none(thread):
        print(f"{colour.yellow}Timer is running. Use .stop() to stop it.{colour.reset}")
    else:
        print(f"{colour.yellow}Timer for thread {thread} is running. Use .stop({thread = }) to stop it.{colour.reset}")

def message_for_action(action: str, thread: str = None) -> None:
    print(f"{colour.yellow}Timer: Something went wrong {action}{'' if helper.thread.is_none(thread) else f' for thread {thread}'}.{colour.reset}")
