"""Test proper parenthetics."""

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


@pytest.mark.parametrize("parens, result", TEXT_WITH_PARENS)
def test_proper_parens(parens, result):
    """Test proper parens returns correct result for given cases."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(parens) == result
