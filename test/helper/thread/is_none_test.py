import pytest
import timer.helper.thread as thread

class TestThreadIsNone():
    def test_real_none(self):
        assert thread.is_none(None) is True
    
    def test_text_none_uppercase(self):
        assert thread.is_none("NONE") is True
    
    def test_text_none_lowercase(self):
        assert thread.is_none("none") is False

    def test_random_text(self):
        assert thread.is_none("something") is False

    def test_random_number(self):
        assert thread.is_none(123) is False
