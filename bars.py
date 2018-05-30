import json
import sys
import argparse
from functools import partial


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF8') as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(loaded_bars):
    return max(
        loaded_bars,
        key=lambda bar:bar['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(loaded_bars):
    return min(
        loaded_bars,
        key=lambda bar:bar['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(loaded_bars, longtitude, latitude):
    return min(
        loaded_bars,
        key=lambda bar: (
                (bar['geometry']['coordinates'][0] - latitude)**2 -
                (bar['geometry']['coordinates'][1] - longtitude)**2
        )
    )


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        action='store',
        dest='filepath',
        help='Filepath with data, "bars.json" by default',
        default='bars.json'
    )
    parser.add_argument(
        '-long',
        type=float,
        action='store',
        dest='longtitude',
        help='You longtitude. If not set it will be generated randomly',
        default='55'
    )
    parser.add_argument(
        '-lat',
        type=float,
        action='store',
        dest='latitude',
        help='You latitude. If not set, it will be generated randomly',
        default='37'
    )
    return parser.parse_args()


if __name__ == '__main__':
    params = parse_arguments()
    loaded_bars = load_data(params.filepath)
    print(get_biggest_bar(loaded_bars)['properties']['Attributes']['Name'])
    print(get_smallest_bar(loaded_bars)['properties']['Attributes']['Name'])
    print(get_closest_bar(loaded_bars, params.longtitude, params.latitude)
          ['geometry']['coordinates'])
