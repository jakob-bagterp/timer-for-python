from os import linesep

from _helper import operating_system

LINESEP = "\n" if operating_system.is_windows() else linesep
