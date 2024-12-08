from abc import ABC, abstractmethod
from types import TracebackType

from .thread_item import ThreadItem


class TimerBase(ABC):
    """Abstract base class of Timer object."""

    __slots__ = ["_decimals", "_threads"]

    def __init__(self) -> None:
        self._decimals: int  # pragma: no cover
        self._threads: list[ThreadItem]  # pragma: no cover

    def __enter__(self) -> "TimerBase":
        raise NotImplementedError  # pragma: no cover

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def start(self, thread: str | None = None, decimals: int | None = None) -> None:
        """Starts the Timer."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def stop(self, thread: str | None = None) -> None:
        """Stops the Timer."""

        raise NotImplementedError  # pragma: no cover
