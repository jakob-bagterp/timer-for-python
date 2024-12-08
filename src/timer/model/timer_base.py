from abc import ABC, abstractmethod
from types import TracebackType

from .thread_item import ThreadItem


class TimerBase(ABC):
    """Abstract base class of Timer object."""

    __slots__ = ["decimals", "threads"]

    def __init__(self) -> None:
        self.decimals: int
        self.threads: list[ThreadItem]

    def __enter__(self) -> "TimerBase":
        raise NotImplementedError

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        raise NotImplementedError

    @abstractmethod
    def start(self, thread: str | None = None, decimals: int | None = None) -> None:
        """Starts the Timer."""

        raise NotImplementedError

    @abstractmethod
    def stop(self, thread: str | None = None) -> None:
        """Stops the Timer."""

        raise NotImplementedError
