"""Tests for even_or_odd function."""


def test_even_or_odd1():
    """Test if it returns Even if given even number."""
    from even_or_odd import even_or_odd
    assert even_or_odd(2) == 'Even'


def test_even_or_odd2():
    """Test if it returns Odd if given odd number."""
    from even_or_odd import even_or_odd
    assert even_or_odd(3) == 'Odd'


def test_even_or_odd3():
    """Test if it returns Even if given even number."""
    from even_or_odd import even_or_odd
    assert even_or_odd(122) == 'Even'


def test_even_or_odd4():
    """Test if it returns Odd if given odd number."""
    from even_or_odd import even_or_odd
    assert even_or_odd(312127) == 'Odd'
