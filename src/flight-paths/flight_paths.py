"""."""

import json
import math
from networkx import Graph, dijkstra_path, dijkstra_path_length


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
            formated_data[city['city'].lower()] = {
                'lat_lon': city['lat_lon'],
                'destination_cities': city['destination_cities']
            }
        return formated_data


def flight_path(start_city, end_city):
    """Generate a flight path using a graph."""
    airports = read_format_and_return()
    start_city = start_city.lower()
    end_city = end_city.lower()
    if start_city not in airports:
        raise ValueError('{} is not a valid start city.'.format(start_city))
    elif end_city not in airports:
        raise ValueError('{} is not a valid destination city.'.format(end_city))
    airports_graph = Graph()
    for city, data in airports.items():
        airports_graph.add_node(city)
        for destination_city in data['destination_cities']:
            destination_city = destination_city.lower()
            try:
                distance = calculate_distance(
                    data['lat_lon'],
                    airports[destination_city]['lat_lon']
                )
            except KeyError:
                continue
            airports_graph.add_edge(city, destination_city, weight=distance)
    path = dijkstra_path(airports_graph, start_city, end_city)
    distance = dijkstra_path_length(airports_graph, start_city, end_city)
    return {"path": [city.title() for city in path], "distance": distance}
