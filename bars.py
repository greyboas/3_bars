import json
import sys


def load_data(filepath):
    bars_seat = []
    bars_coordinate = []
    try:
        with open(filepath, 'r') as file_handler:
            loaded_json = json.load(file_handler)
        for f in loaded_json.get('features'):
            bars_seat.append(
                f.get('properties')
                    .get('Attributes')
                    .get('SeatsCount'))
            bars_coordinate.append(
                f.get('geometry')
                    .get('coordinates'))
        return loaded_json, bars_seat, bars_coordinate
    except ValueError:
        return None


def get_biggest_bar(loaded_json, bars_seat):
    for bar in loaded_json.get('features'):
        if bar.get('properties')\
                .get('Attributes')\
                .get('SeatsCount') == max(bars_seat):
            biggest_bar_name = bar.get('properties').\
                get('Attributes')\
                .get('Name')
    return biggest_bar_name, max(bars_seat)


def get_smallest_bar(loaded_json, bars_seat):
    for bar in loaded_json.get('features'):
        if bar.get('properties')\
                .get('Attributes')\
                .get('SeatsCount') == min(bars_seat):
            smallest_bar_name = bar.get('properties')\
                .get('Attributes')\
                .get('Name')
    return smallest_bar_name, min(bars_seat)


def get_closest_bar(loaded_json, bars_coordinate):
    delta_distance = []
    for coordinate in bars_coordinate:
        delta_distance.append((abs(coordinate[0]-longitude)) +
                              (abs(coordinate[1]-latitude)))
    for bar in loaded_json.get('features'):
        if bar == loaded_json.get('features')[delta_distance
                .index(min(delta_distance))]:
            closest_bar_name = bar.get('properties')\
                .get('Attributes')\
                .get('Name')
    return closest_bar_name, coordinate


if __name__ == '__main__':
    try:
        filepath = 'bar.json'
        loaded_json, bars_seat, bars_coordinate = load_data(filepath)
    except IndexError:
        sys.exit('Not set argyment filepath')
    except FileNotFoundError:
        sys.exit('File not found')
    try:
        longitude = float(sys.argv[1])
        latitude = float(sys.argv[2])
    except IndexError:
        sys.exit('Not set argyment coordinate')
    except ValueError:
        sys.exit('The argument format is not valid (For example, '
                 'longitude 37.594104911195 or latitude 55.748861154831935)')
    print(get_biggest_bar(loaded_json, bars_seat))
    print(get_smallest_bar(loaded_json, bars_seat))
    print(get_closest_bar(loaded_json, bars_coordinate))



