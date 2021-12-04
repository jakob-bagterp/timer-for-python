import numpy
from timer.constants.decimals import default as default_decimals
import timer.helper.decimals as decimals

class TestDecimalsValidationAndNormalisation():
    def test_range_0_10(self):
        for input in range(0, 10):
            assert decimals.validate_and_normalise(input) == input
    
    def test_number_larger_than_9_should_default(self):
        for input in range(10, 100):
            assert decimals.validate_and_normalise(input) == 9

    def test_negative_number_should_default(self):
        for input in range(-1, -100):
            assert decimals.validate_and_normalise(input) == default_decimals()
    
    def test_float_should_default(self):
        assert decimals.validate_and_normalise(3.5) == 2
        assert decimals.validate_and_normalise(-10.1) == 2

    def test_negative_float_should_default(self):
        for input in numpy.arange(-100, 0, 0.1):
            assert decimals.validate_and_normalise(input) == default_decimals()

    def test_text_should_default(self):
        assert decimals.validate_and_normalise("10") == default_decimals()
        assert decimals.validate_and_normalise("1") == default_decimals()
        assert decimals.validate_and_normalise("abc") == default_decimals()
