"""Tests for double_char function."""


def test_double_char_1():
    """Return a string with twice the amount of charecters given (in order)."""
    from double_char import double_char
    assert double_char('Amos') == 'AAmmooss'


def test_double_char_2():
    """Return a string with twice the amount of charecters given (in order)."""
    from double_char import double_char
    assert double_char('sAm') == 'ssAAmm'


def test_double_char_3():
    """Return a string with twice the amount of charecters given (in order)."""
    from double_char import double_char
    assert double_char('DuDe') == 'DDuuDDee'


def test_double_char_4():
    """Return a string with twice the amount of charecters given (in order)."""
    from double_char import double_char
    assert double_char('Hello_World') == 'HHeelllloo__WWoorrlldd'
