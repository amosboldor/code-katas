"""Test for counting_sheep."""


def test_count_sheeps1():
    """Return number of trues in list."""
    from counting_sheep import count_sheeps
    assert count_sheeps([
        True, True, True, False,
        True, True, True, True,
        True, False, True, False,
        True, False, False, True,
        True, True, True, True,
        False, False, True, True]) == 17


def test_count_sheeps2():
    """Return number of trues in list."""
    from counting_sheep import count_sheeps
    assert count_sheeps([
        True, True, True, False,
        True, True, True, True,
        True, True, True, True,
        True, True, False, True,
        True, True, True, True,
        False, False, True, True]) == 20


def test_count_sheeps3():
    """Return number of trues in list."""
    from counting_sheep import count_sheeps
    assert count_sheeps([
        True, True, True, False,
        True, True, True, True,
        True, False, True, False,
        True, False, False, True,
        True, True, False, False,
        False, False, True, True]) == 15


def test_count_sheeps4():
    """Return number of trues in list."""
    from counting_sheep import count_sheeps
    assert count_sheeps([
        True, True, True, False,
        True, True, True, True,
        True, False, False, False,
        True, False, False, True,
        True, True, True, True,
        False, False, True, True]) == 16
