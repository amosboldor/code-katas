"""Tests for greet function."""


def test_greet1():
    """Return Hello, my love! if argument is Jonny else Hello, name!."""
    from jennys_secret_message import greet
    assert greet("Johnny") == 'Hello, my love!'


def test_greet2():
    """Return Hello, my love! if argument is Jonny else Hello, name!."""
    from jennys_secret_message import greet
    assert greet("Amos") == 'Hello, Amos!'


def test_greet3():
    """Return Hello, my love! if argument is Jonny else Hello, name!."""
    from jennys_secret_message import greet
    assert greet("Jack") == 'Hello, Jack!'


def test_greet4():
    """Return Hello, my love! if argument is Jonny else Hello, name!."""
    from jennys_secret_message import greet
    assert greet("Bob") == 'Hello, Bob!'
