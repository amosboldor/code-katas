"""Tests for square_sum function."""


def test_square_sum1():
    """Test that squared_sum returns sum of every squared number in list."""
    from squared_sum import square_sum
    assert square_sum([1, 2]) == 5


def test_square_sum2():
    """Test that squared_sum returns sum of every squared number in list."""
    from squared_sum import square_sum
    assert square_sum([0, 3, 4, 5]) == 50


def test_square_sum3():
    """Test that squared_sum returns sum of every squared number in list."""
    from squared_sum import square_sum
    assert square_sum([20, -17, -5]) == 714


def test_square_sum4():
    """Test that squared_sum returns sum of every squared number in list."""
    from squared_sum import square_sum
    assert square_sum([1, 3]) == 10
