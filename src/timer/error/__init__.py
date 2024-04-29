__all__: list[str] = []

from colorist import Color

from .. import helper
from ..model.timer_base import TimerBase


def start_controller(thread: str | None) -> None:
    if helper.thread.is_none(thread):
        print(f"{Color.YELLOW}Timer is running. Use .stop() to stop it.{Color.OFF}")
    else:
        print(f"{Color.YELLOW}Timer for thread {thread} is running. Use .stop({thread=}) to stop it.{Color.OFF}")


def stop_controller(timer: TimerBase, thread: str | None) -> None:
    if helper.thread.is_none(thread):
        print(f"{Color.YELLOW}Timer is not running. Use .start() to start it.{Color.OFF}")
    else:
        print(f"{Color.YELLOW}Timer for thread {thread} is not running. Use .start({thread=}) to start it.{Color.OFF}")
    if len(timer.threads) > 0:
        open_threads = [thread_item.name for thread_item in timer.threads]
        print(f"Or maybe you aren't stopping the right thread? Currently open threads: {', '.join(open_threads)}")


def message_for_action(action: str, thread: str | None = None) -> None:
    print(f"{Color.YELLOW}Timer: Something went wrong {action}{'' if helper.thread.is_none(thread) else f' for thread {thread}'}.{Color.OFF}")
