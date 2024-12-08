from abc import ABC, abstractmethod

from .thread_item import ThreadItem


class TimerBase(ABC):
    """Abstract base class of Timer object."""

    __slots__ = ["decimals", "threads"]

    def __init__(self) -> None:
        self.decimals: int  # pragma: no cover
        self.threads: list[ThreadItem]  # pragma: no cover

    @abstractmethod
    def start(self, thread: str, decimals: int) -> None:
        """Starts the Timer."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def stop(self, thread: str) -> None:
        """Stops the Timer."""

        raise NotImplementedError  # pragma: no cover
