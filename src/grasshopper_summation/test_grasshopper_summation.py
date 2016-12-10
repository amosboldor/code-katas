"""Tests for summation function."""


def test_summation1():
    """Test if return summation of every number between 1 and num."""
    from grasshopper_summation import summation
    assert summation(1) == 1


def test_summation2():
    """Test if return summation of every number between 1 and num."""
    from grasshopper_summation import summation
    assert summation(8) == 36


def test_summation3():
    """Test if return summation of every number between 1 and num."""
    from grasshopper_summation import summation
    assert summation(2) == 3


def test_summation4():
    """Test if return summation of every number between 1 and num."""
    from grasshopper_summation import summation
    assert summation(4) == 10
