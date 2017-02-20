"""Test flight_paths.py."""

from flight_paths import read_format_and_return


def test_read_format_and_return():
    """Test read format and return."""
    data = read_format_and_return()
    assert data['Seattle']


def test_read_format_and_return_has_correct_data():
    """Test read format and return."""
    data = read_format_and_return()
    assert 'lat_lon' in data['Seattle']
    assert 'destination_cities' in data['Seattle']
