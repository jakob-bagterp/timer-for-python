__all__ = ["start_controller", "stop_controller", "message_for_action"]

from .. import helper
from ..helper.colour import Colour
from ..model.timer import TimerObject

def start_controller(thread: str | None) -> None:
    if helper.thread.is_none(thread):
        print(f"{Colour.YELLOW}Timer is running. Use .stop() to stop it.{Colour.RESET}")
    else:
        print(f"{Colour.YELLOW}Timer for thread {thread} is running. Use .stop({thread = }) to stop it.{Colour.RESET}")

def stop_controller(timer: TimerObject, thread: str| None) -> None:
    if helper.thread.is_none(thread):
        print(f"{Colour.YELLOW}Timer is not running. Use .start() to start it.{Colour.RESET}")
    else:
        print(f"{Colour.YELLOW}Timer for thread {thread} is not running. Use .start({thread = }) to start it.{Colour.RESET}")
    if len(timer.threads) > 0:
        open_threads = [thread_item.name for thread_item in timer.threads]
        print(f"Or maybe you aren't stopping the right thread? Currently open threads: {', '.join(open_threads)}")

def message_for_action(action: str, thread: str | None = None) -> None:
    print(f"{Colour.YELLOW}Timer: Something went wrong {action}{'' if helper.thread.is_none(thread) else f' for thread {thread}'}.{Colour.RESET}")
