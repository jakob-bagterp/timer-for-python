from _helper.range import generate_range
from _mock_data.decimals import DECIMALS_RANGE

from timer.constant.decimals import DEFAULT, MAXIMUM, MINIMUM
from timer.helper.decimals import validate_and_normalise


def test_number_from_minimum_to_maximum() -> None:
    for decimals in DECIMALS_RANGE:
        assert validate_and_normalise(decimals) == decimals


def test_number_larger_than_maximum_should_default() -> None:
    for decimals in range(MAXIMUM + 1, 100):
        assert validate_and_normalise(decimals) == MAXIMUM


def test_negative_number_should_default() -> None:
    for decimals in range(-100, 0):
        assert validate_and_normalise(decimals) == DEFAULT


def test_float_within_minimum_to_maximum_should_not_default() -> None:
    for decimals in generate_range(MINIMUM, MAXIMUM + 0.4, 0.1):
        assert validate_and_normalise(decimals) == int(round(decimals))


def test_float_larger_than_maximum_should_default() -> None:
    for decimals in generate_range(MAXIMUM + 0.5, 100, 0.1):
        assert validate_and_normalise(decimals) == MAXIMUM


def test_negative_float_should_default() -> None:
    for decimals in generate_range(-100, 0, 0.1):
        assert validate_and_normalise(decimals) == DEFAULT


def test_text_should_default() -> None:
    assert validate_and_normalise("10") == DEFAULT
    assert validate_and_normalise("1") == DEFAULT
    assert validate_and_normalise("abc") == DEFAULT
