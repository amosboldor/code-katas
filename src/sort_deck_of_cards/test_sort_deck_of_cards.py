"""Tests for sort_deck_of_cards program."""

import pytest

DECKS = [
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')]
]


@pytest.mark.parametrize('unsorted, sorted', DECKS)
def test_sort_deck_of_cards(unsorted, sorted):
    """Test that function sorts cards."""
    from sort_deck_of_cards import sort_cards
    assert sort_cards(unsorted) == sorted
