import json
import argparse
import os
from geopy.distance import vincenty



def get_my_location():
    parser = argparse.ArgumentParser()
    parser.add_argument('langitute', type=float)
    parser.add_argument('lattitute', type=float)
    return parser.parse_args()


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_seats_count(bar):
    return bar['Cells']['SeatsCount']


def get_distance(bar):
    my_location = []
    bars_coordinate = bar['Cells']['geoData']['coordinates']
    my_coordinate = get_my_location()
    my_langitute = my_coordinate.langitute
    my_lattitute = my_coordinate.lattitute
    my_location.append([my_langitute, my_lattitute])
    distance = vincenty(bars_coordinate, my_location).miles
    return distance


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=get_seats_count)
    return biggest_bar['Cells']['Name']


def get_smallest_bar(bars):
    smallest_bar = min(bars, key=get_seats_count)
    return smallest_bar['Cells']['Name']


def get_closest_bar(bars):
    closest_bar = min(bars, key=get_distance)
    return closest_bar['Cells']['Name']



if __name__ == '__main__':
    bars = load_data('input a path')
    print('The biggest bar:', get_biggest_bar(bars))
    print('The smallest bar:', get_smallest_bar(bars))
    print('The closest bar:', get_closest_bar(bars))