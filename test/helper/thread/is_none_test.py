import timer.helper.thread as thread

class TestThreadIsNone():
    def test_real_none(self) -> None:
        assert thread.is_none(None) is True
    
    def test_text_none_uppercase(self) -> None:
        assert thread.is_none("NONE") is True
    
    def test_text_none_lowercase(self) -> None:
        assert thread.is_none("none") is False

    def test_random_text(self) -> None:
        assert thread.is_none("something") is False

    def test_random_number(self) -> None:
        assert thread.is_none(123) is False
