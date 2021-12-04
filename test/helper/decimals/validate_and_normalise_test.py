import numpy
from timer.constants import decimals
from timer.helper.decimals import validate_and_normalise

class TestDecimalsValidationAndNormalisation():
    def test_range_0_10(self):
        for input in range(0, decimals.maximum() + 1):
            assert validate_and_normalise(input) == input
    
    def test_number_larger_than_9_should_default(self):
        for input in range(decimals.maximum() + 1, 100):
            assert validate_and_normalise(input) == decimals.maximum()

    def test_negative_number_should_default(self):
        for input in range(-1, -100):
            assert validate_and_normalise(input) == decimals.default()
    
    def test_float_should_default(self):
        assert decimals.validate_and_normalise(3.5) == 2
        assert decimals.validate_and_normalise(-10.1) == 2

    def test_negative_float_should_default(self):
        for input in numpy.arange(-100, 0, 0.1):
            assert validate_and_normalise(input) == decimals.default()

    def test_text_should_default(self):
        assert validate_and_normalise("10") == decimals.default()
        assert validate_and_normalise("1") == decimals.default()
        assert validate_and_normalise("abc") == decimals.default()
