import numpy
from timer.constant.decimals import DEFAULT, MAXIMUM, MINIMUM 
from timer.helper.decimals import validate_and_normalise

class TestDecimalsValidationAndNormalisation():
    def test_number_from_minimum_to_maximum(self) -> None:
        for decimals in range(MINIMUM, MAXIMUM + 1):
            assert validate_and_normalise(decimals) == decimals
    
    def test_number_larger_than_maximum_should_default(self) -> None:
        for decimals in range(MAXIMUM + 1, 100):
            assert validate_and_normalise(decimals) == MAXIMUM

    def test_negative_number_should_default(self) -> None:
        for decimals in range(-1, -100):
            assert validate_and_normalise(decimals) == DEFAULT
    
    def test_float_within_minimum_to_maximum_should_not_default(self) -> None:
        for decimals in numpy.arange(MINIMUM, MAXIMUM + 0.4, 0.1):
            assert validate_and_normalise(decimals) == int(round(decimals))

    def test_float_larger_than_maximum_should_default(self) -> None:
        for decimals in numpy.arange(MAXIMUM + 0.5, 100, 0.1):
            assert validate_and_normalise(decimals) == MAXIMUM

    def test_negative_float_should_default(self) -> None:
        for decimals in numpy.arange(-100, 0, 0.1):
            assert validate_and_normalise(decimals) == DEFAULT

    def test_text_should_default(self) -> None:
        assert validate_and_normalise("10") == DEFAULT
        assert validate_and_normalise("1") == DEFAULT
        assert validate_and_normalise("abc") == DEFAULT
