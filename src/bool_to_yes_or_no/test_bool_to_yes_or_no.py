"""Tests for bool_to_word function."""


def test_bool_to_word1():
    """Should return Yes for True and No for False."""
    from bool_to_yes_or_no import bool_to_word
    assert bool_to_word(True) == 'Yes'


def test_bool_to_word2():
    """Should return Yes for True and No for False."""
    from bool_to_yes_or_no import bool_to_word
    assert bool_to_word(False) == 'No'
