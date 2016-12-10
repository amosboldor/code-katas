"""Tests for count_positives_sum_negatives function."""


def test_count_positives_sum_negatives1():
    """Return list of count of positives numbers & sum of negative numbers."""
    from count_positives_sum_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([
        1, 2, 3, 4, 5, 6, 7, 8, 9,
        10, -11, -12, -13, -14, -15]) == [10, -65]


def test_count_positives_sum_negatives2():
    """Return list of count of positives numbers & sum of negative numbers."""
    from count_positives_sum_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([
        0, 2, 3, 0, 5, 6, 7, 8,
        9, 10, -11, -12, -13, -14]) == [8, -50]


def test_count_positives_sum_negatives3():
    """Return list of count of positives numbers & sum of negative numbers."""
    from count_positives_sum_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([1]) == [1, 0]


def test_count_positives_sum_negatives4():
    """Return list of count of positives numbers & sum of negative numbers."""
    from count_positives_sum_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]


def test_count_positives_sum_negatives5():
    """Return list of count of positives numbers & sum of negative numbers."""
    from count_positives_sum_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([]) == []
