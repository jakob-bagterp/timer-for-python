from timer.constant.various import NONE_VALUE
import timer.helper.thread as thread

class TestNormalisationToStringAndUppercase():
    def test_real_none(self) -> None:
        assert thread.normalise_to_string_and_uppercase(None) == NONE_VALUE
    
    def test_text_none_uppercase(self) -> None:
        assert thread.normalise_to_string_and_uppercase("NONE") == NONE_VALUE
    
    def test_text_none_lowercase(self) -> None:
        assert thread.normalise_to_string_and_uppercase("none") == NONE_VALUE

    def test_text_thread(self) -> None:
        assert thread.normalise_to_string_and_uppercase("thread a") == "THREAD A"
        assert thread.normalise_to_string_and_uppercase("tHreaD B") == "THREAD B"

    def test_number_to_string(self) -> None:
        assert thread.normalise_to_string_and_uppercase(123) == "123"
