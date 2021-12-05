import numpy
from timer.constants.decimals import default, maximum, minimum 
from timer.helper.decimals import validate_and_normalise

class TestDecimalsValidationAndNormalisation():
    def test_number_from_minimum_to_maximum(self):
        for decimals in range(minimum(), maximum() + 1):
            assert validate_and_normalise(decimals) == decimals
    
    def test_number_larger_than_maximum_should_default(self):
        for decimals in range(maximum() + 1, 100):
            assert validate_and_normalise(decimals) == maximum()

    def test_negative_number_should_default(self):
        for decimals in range(-1, -100):
            assert validate_and_normalise(decimals) == default()
    
    def test_float_within_minimum_to_maximum_should_not_default(self):
        for decimals in numpy.arange(minimum(), maximum() + 0.4, 0.1):
            assert validate_and_normalise(decimals) == int(round(decimals))

    def test_float_larger_than_maximum_should_default(self):
        for decimals in numpy.arange(maximum() + 0.5, 100, 0.1):
            assert validate_and_normalise(decimals) == maximum()

    def test_negative_float_should_default(self):
        for decimals in numpy.arange(-100, 0, 0.1):
            assert validate_and_normalise(decimals) == default()

    def test_text_should_default(self):
        assert validate_and_normalise("10") == default()
        assert validate_and_normalise("1") == default()
        assert validate_and_normalise("abc") == default()
