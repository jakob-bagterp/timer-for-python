__all__ = ["message_for_action"]

import helper.thread

from text_colour import TextColour
colour = TextColour()

def message_for_action(action: str, thread: str = None) -> None:
    print(f"{colour.yellow}Timer: Something went wrong {action}{'' if helper.thread.is_none(thread) else f' for thread {thread}'}.{colour.reset}")
