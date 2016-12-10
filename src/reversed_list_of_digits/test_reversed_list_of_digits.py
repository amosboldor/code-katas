"""Test digitize function."""


def test_digitize1():
    """Digitize should return reversed array of digits."""
    from reversed_list_of_digits import digitize
    assert digitize(35231) == [1, 3, 2, 5, 3]


def test_digitize2():
    """Digitize should return reversed array of digits."""
    from reversed_list_of_digits import digitize
    assert digitize(123) == [3, 2, 1]


def test_digitize3():
    """Digitize should return reversed array of digits."""
    from reversed_list_of_digits import digitize
    assert digitize(425666) == [6, 6, 6, 5, 2, 4]


def test_digitize4():
    """Digitize should return reversed array of digits."""
    from reversed_list_of_digits import digitize
    assert digitize(19329) == [9, 2, 3, 9, 1]
