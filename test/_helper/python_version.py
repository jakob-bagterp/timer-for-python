from platform import python_version


def is_3_10() -> bool:
    return python_version().startswith("3.10")  # pragma: no cover


def is_3_11() -> bool:
    return python_version().startswith("3.11")  # pragma: no cover


def is_3_12() -> bool:
    return python_version().startswith("3.12")  # pragma: no cover


def is_3_13() -> bool:
    return python_version().startswith("3.13")  # pragma: no cover
