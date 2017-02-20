"""Test flight_paths.py."""

from flight_paths import read_format_and_return
from flight_paths import flight_path


def test_read_format_and_return():
    """Test read format and return."""
    data = read_format_and_return()
    assert data['seattle']


def test_read_format_and_return_has_correct_data():
    """Test read format and return."""
    data = read_format_and_return()
    assert 'lat_lon' in data['seattle']
    assert 'destination_cities' in data['seattle']


def test_flight_path_returns_right_cities():
    """Test if flight_path returns expected cities."""
    data = flight_path('Seattle', 'New York City')
    assert 'Seattle' in data["path"] and 'New York City' in data["path"]


def test_flight_path_returns_right_cities_seattle_dinard():
    """Test if flight_path returns expected cities (bigger path)."""
    data = flight_path('Seattle', 'Dinard')
    path = ['Seattle', 'Vancouver', 'Dublin', 'East Midlands', 'Dinard']
    assert path == data["path"]
