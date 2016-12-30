"""Test proper parenthetics module."""

import pytest


TEXT_WITH_PARENS = [
    ['()()()', 0],
    ['())()(', -1],
    ['))((', -1],
    ['(hello)(world)', 0],
    ['(((())', 1],
    ['()((())))', -1],
    ['()(()(()(', 1],
    [')', -1],
    ['(', 1],
    ['((((WAT(((((', 1]
]


@pytest.mark.parametrize("text, result", TEXT_WITH_PARENS)
def test_proper_parenthetics(text, result):
    """Test proper_parenthetics returns correct result for given text."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(text) == result
