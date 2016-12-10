"""Test positive_sum function."""


def test_positive_sum1():
    """Should return the sum of all the numbers that are positive."""
    from sum_of_positive import positive_sum
    assert positive_sum([-1, 2, 3, 4, -5]) == 9


def test_positive_sum2():
    """Should return the sum of all the numbers that are positive."""
    from sum_of_positive import positive_sum
    assert positive_sum([1, 2, 3, 4, -5]) == 10


def test_positive_sum3():
    """Should return the sum of all the numbers that are positive."""
    from sum_of_positive import positive_sum
    assert positive_sum([-1, -2, 3, 4, -5]) == 7


def test_positive_sum4():
    """Should return the sum of all the numbers that are positive."""
    from sum_of_positive import positive_sum
    assert positive_sum([-1, -2, -3, 4, -5]) == 4
