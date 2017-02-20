"""."""

import json
import math


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.

    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.
    """
    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934


def read_format_and_return():
    """Read and format and return the data from json file."""
    with open('cities_with_airports.json', 'r') as file:
        airports = json.load(file)
        formated_data = {}
        for city in airports:
            formated_data[city['city']] = {
                'lat_lon': city['lat_lon'],
                'destination_cities': city['destination_cities']
            }
        return formated_data
