from timer import Timer


def ensure_all_timer_threads_are_stopped() -> None:
    """Ensures all threads are stopped."""

    Timer().threads = []
    assert len(Timer().threads) == 0
