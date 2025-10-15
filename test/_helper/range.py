def generate_range(start: float, stop: float, step: float = 1) -> list[float]:
    """Generate a range of numbers."""

    return [start + i * step for i in range(int((stop - start) / step))]
