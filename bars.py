import json
import sys


def load_data(filepath):
    bars_seat = []
    bars_coordinate = []
    with open(filepath, 'r') as file_handler:
        data = json.load(file_handler)
        for f in data.get('features'):
            bars_seat.append(f.get('properties').get('Attributes')
                             .get('SeatsCount'))
            bars_coordinate.append(f.get('geometry').get('coordinates'))
    return data, bars_seat, bars_coordinate


def get_biggest_bar(filepath):
    data, bars_seat, bars_coordinate = load_data(filepath)
    for bar in data.get('features'):
        if bar.get('properties').get('Attributes')\
                .get('SeatsCount') == max(bars_seat):
            biggest_bar_name = bar.get('properties').get('Attributes')\
                .get('Name')
    return biggest_bar_name, max(bars_seat)


def get_smallest_bar(filepath):
    data, bars_seat, bars_coordinate = load_data(filepath)
    for bar in data.get('features'):
        if bar.get('properties').get('Attributes')\
                .get('SeatsCount') == min(bars_seat):
            smallest_bar_name = bar.get('properties').get('Attributes')\
                .get('Name')
    return smallest_bar_name, min(bars_seat)


def get_closest_bar(filepath, longitude, latitude):
    data, bars_seat, bars_coordinate = load_data(filepath)
    delta_distance = []
    for coordinate in bars_coordinate:
        delta_distance.append((abs(coordinate[0]-longitude)) +
                              (abs(coordinate[1]-latitude)))
    for bar in data.get('features'):
        if bar == data.get('features')[delta_distance
                .index(min(delta_distance))]:
            closest_bar_name = bar.get('properties').get('Attributes')\
                .get('Name')
    return closest_bar_name, coordinate


if __name__ == '__main__':
    filepath = 'bar.json'
    longitude = 37.594104911195
    latitude = 55.748861154831935
    print(get_biggest_bar(filepath))
    print(get_smallest_bar(filepath))
    print(get_closest_bar(filepath, longitude, latitude))
