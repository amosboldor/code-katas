"""Test for sum_array function."""


def test_sum_array1():
    """Sum of the numbers of the array except the highest and lowest number."""
    from sum_without_high_and_low import sum_array
    assert sum_array([6, 2, 1, 8, 10]) == 16


def test_sum_array2():
    """Sum of the numbers of the array except the highest and lowest number."""
    from sum_without_high_and_low import sum_array
    assert sum_array([6, 2, 13, 8, 10]) == 24


def test_sum_array3():
    """Sum of the numbers of the array except the highest and lowest number."""
    from sum_without_high_and_low import sum_array
    assert sum_array([6, 2, 1, 8, 10]) == 16


def test_sum_array4():
    """Sum of the numbers of the array except the highest and lowest number."""
    from sum_without_high_and_low import sum_array
    assert sum_array([6, 0, 1, 8, 10]) == 15
