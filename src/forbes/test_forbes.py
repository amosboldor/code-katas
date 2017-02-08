"""Test for get_oldest_and_youngest_billionaire function."""

from forbes import get_oldest_and_youngest_billionaire


def test_get_oldest_and_youngest_billionaire_returns_youngest():
    """Test get oldest and youngest billionaire returns youngest."""
    data = get_oldest_and_youngest_billionaire('forbes_billionaires_2016.json')
    assert data["Billionaire with Lowest Age"]['name'] == 'Mark Zuckerberg'


def test_getoldest_and_youngest_billionaire_returns_youngest_oldest_info():
    """Test get oldest and youngest billionaire returns youngest info."""
    data = get_oldest_and_youngest_billionaire('forbes_billionaires_2016.json')
    assert data["Billionaire with Lowest Age"]['net_worth (USD)'] == 44600000000
    assert data["Billionaire with Lowest Age"]['industry'] == 'Facebook'


def test_get_oldest_and_youngest_billionaire_returns_oldest():
    """Test get oldest and youngest billionaire returns oldest."""
    data = get_oldest_and_youngest_billionaire('forbes_billionaires_2016.json')
    assert data["Billionaire with Highest Age"]['name'] == 'Phil Knight'


def test_get_oldest_and_youngest_billionaire_returns_youngest_youngest_info():
    """Test get youngest and youngest billionaire returns youngest info."""
    data = get_oldest_and_youngest_billionaire('forbes_billionaires_2016.json')
    assert data["Billionaire with Highest Age"]['net_worth (USD)'] == 24400000000
    assert data["Billionaire with Highest Age"]['industry'] == 'Nike'
