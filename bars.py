import json
import os
from geopy.distance import vincenty


my_location = []
my_langitute = float(input('Please input latitude:'))
my_lattitute = float(input('Please input longitude:'))
my_location.append([my_langitute, my_lattitute])


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_seats_count(bar):
    return bar['Cells']['SeatsCount']


def get_distance(bar):
    bars_coordinate = bar['Cells']['geoData']['coordinates']
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
    bars = load_data('put_a_path')
    print('The biggest bar:', get_biggest_bar(bars))
    print('The smallest bar:', get_smallest_bar(bars))
    print('The closest bar:', get_closest_bar(bars))