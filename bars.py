import json
import sys
import math


def load_data(filepath):
    bars_seat = []
    bars_coordinate =[]
    with open(filepath, 'r') as file_handler:
        data = json.load(file_handler)
        for f in data.get('features'):
            bars_seat.append(f.get('properties').
                            get('Attributes').get('SeatsCount'))
            bars_coordinate.append(f.get('geometry').get('coordinates'))
    return data, bars_seat, bars_coordinate


def get_biggest_bar(filepath):
    data, bars_seat, bars_coordinate = load_data(filepath)
    for f in data.get('features'):
        if f.get('properties').get('Attributes').get('SeatsCount') == max(bars_seat):
            d = f.get('properties').get('Attributes').get('Name')
    return "Название самого большого бара: {} Посадочных мест: {}".format(d,max(bars_seat))


def get_smallest_bar(filepath):
    data, bars_seat, bars_coordinate = load_data(filepath)
    for f in data.get('features'):
        if f.get('properties').get('Attributes').get('SeatsCount') == min(bars_seat):
            d = f.get('properties').get('Attributes').get('Name')
    return "Название самого маленького бара: {} Посадочных мест: {}".format(d, min(bars_seat))


def get_closest_bar(filepath, longitude, latitude):
    data, bars_seat, bars_coordinate = load_data(filepath)
    i = []
    for c in bars_coordinate:
        i.append((abs(c[0]-longitude))   + (abs(c[1]-latitude))**2)
    c = data.get('features')[i.index(min(i))]
    return c

if __name__ == '__main__':
    filepath = sys.argv[1]
    longitude = 37.594104911195
    latitude = 55.748861154831935
    print(get_biggest_bar(filepath))
    print(get_smallest_bar(filepath))
    print(get_closest_bar(filepath, longitude, latitude))



