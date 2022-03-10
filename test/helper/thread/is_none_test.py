import timer.helper.thread as thread


def test_real_none() -> None:
    assert thread.is_none(None) is True


def test_text_none_uppercase() -> None:
    assert thread.is_none("NONE") is True


def test_text_none_lowercase() -> None:
    assert thread.is_none("none") is False


def test_random_text() -> None:
    assert thread.is_none("something") is False


def test_random_number() -> None:
    assert thread.is_none(123) is False
