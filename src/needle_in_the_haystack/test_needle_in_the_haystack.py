"""Tests find_needle function."""


def test_find_needle1():
    """Return found the needle at position _."""
    from needle_in_the_haystack import find_needle
    assert find_needle([
        '3',
        '123124234',
        None,
        'needle',
        'world',
        'hay',
        2,
        '3',
        True,
        False]) == 'found the needle at position 3'


def test_find_needle2():
    """Return found the needle at position _."""
    from needle_in_the_haystack import find_needle
    assert find_needle([
        'needle',
        '123124234',
        None,
        '3',
        'world',
        'hay',
        2,
        '3',
        True,
        False]) == 'found the needle at position 0'


def test_find_needle3():
    """Return found the needle at position _."""
    from needle_in_the_haystack import find_needle
    assert find_needle([
        '3',
        '123124234',
        None,
        'world',
        'needle',
        'hay',
        2,
        '3',
        True,
        False]) == 'found the needle at position 4'


def test_find_needle4():
    """Return found the needle at position _."""
    from needle_in_the_haystack import find_needle
    assert find_needle([
        '3',
        '123124234',
        None,
        '3',
        'world',
        'hay',
        2,
        'needle',
        True,
        False]) == 'found the needle at position 7'
