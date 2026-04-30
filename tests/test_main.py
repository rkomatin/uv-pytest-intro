import pytest
from main import is_even


def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(3) is False


def test_is_even_with_zero():
    assert is_even(0) is True


def test_is_even_with_negative_even():
    assert is_even(-2) is True


def test_is_even_with_negative_odd():
    assert is_even(-7) is False


def test_is_even_with_float():
    with pytest.raises(TypeError):
        is_even(1.5)


def test_is_even_with_string():
    with pytest.raises(TypeError):
        is_even("4")
