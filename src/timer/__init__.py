__all__ = ["function_timer", "Timer"]

from .decorator.benchmark import function_timer
from .model.timer import Timer
from .version import __version__  # noqa
