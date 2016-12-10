"""Tests for opposite."""


def test_opposite1():
    """Return a positive if given negative and vis versa."""
    from opposite_number import opposite
    assert opposite(1) == -1.0


def test_opposite2():
    """Return a positive if given negative and vis versa."""
    from opposite_number import opposite
    assert opposite(-11) == 11.0


def test_opposite3():
    """Return a positive if given negative and vis versa."""
    from opposite_number import opposite
    assert opposite(1231) == -1231.0


def test_opposite4():
    """Return a positive if given negative and vis versa."""
    from opposite_number import opposite
    assert opposite(-123.1) == 123.1
