import sys


def is_linux() -> bool:
    return sys.platform.startswith("linux")  # pragma: no cover


def is_macos() -> bool:
    return sys.platform.startswith("darwin")  # pragma: no cover


def is_windows() -> bool:
    return sys.platform.startswith("win32")  # pragma: no cover
