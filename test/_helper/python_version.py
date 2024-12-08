from platform import python_version


def is_3_10() -> bool:
    return python_version().startswith("3.10.")


def is_3_11() -> bool:
    return python_version().startswith("3.11.")


def is_3_12() -> bool:
    return python_version().startswith("3.12.")


def is_3_13() -> bool:
    return python_version().startswith("3.13.")
