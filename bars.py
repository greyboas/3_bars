import json
import sys
import argparse
from functools import partial


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF8') as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(loaded_bars):
    return max(loaded_bars,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount']
               )


def get_smallest_bar(loaded_bars):
    return min(loaded_bars,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount']
               )


def validation_longitude_latitude(dirty_latitude, dirty_longtitude):
    latitude = float(dirty_latitude)
    longtitude = float(dirty_longtitude)
    return latitude, longtitude


def get_closest_bar(loaded_bars, longitude, latitude):
    return min(loaded_bars,
               key=lambda bar: (
                       (bar['geometry']['coordinates'][0] - longitude)**2 -
                       (bar['geometry']['coordinates'][1] - latitude)**2)
               )


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', action='store',
        dest='filepath',
        help='Filepath with data, "bars.json" by default',
        default='bars.json'
    )
    parser.add_argument(
        '-lat', action='store',
        dest='dirty_latitude',
        help='You latitude. If not set, it will be generated randomly',
        default='37'
    )
    parser.add_argument(
        '-long', action='store',
        dest='dirty_longtitude',
        help='You longtitude. If not set it will be generated randomly',
        default='55'
    )

    return parser.parse_args()


if __name__ == '__main__':
    params = parse_arguments()
    loaded_bars = load_data(params.filepath)
    try:
        longitude, latitude = validation_longitude_latitude(
            params.dirty_latitude,
            params.dirty_longtitude)
    except IndexError:
        print('Not set argyment coordinate')
    except ValueError:
        print('The argument format is not valid (For example, '
              'longitude 37.594104911195 or latitude 55.748861154831935)')
    print(get_biggest_bar(loaded_bars)['properties']['Attributes']['Name'])
    print(get_smallest_bar(loaded_bars)['properties']['Attributes']['Name'])
    print(get_closest_bar(loaded_bars, longitude, latitude)
          ['properties']['Attributes']['Name'])
