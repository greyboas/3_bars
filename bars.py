import json
import sys

bar_seat = []
filepath = sys.argv[1]

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        data = json.load(file_handler)

    return data

def get_biggest_bar(filepath):
    data1 = load_data(filepath)
    for f in data1.get('features'):
        bar_seat.append(f.get('properties').get('Attributes').get('SeatsCount'))
    for f in data1.get('features'):
        if f.get('properties').get('Attributes').get('SeatsCount') == max(bar_seat):
            d = f.get('properties').get('Attributes').get('Name')
    return "Название самого большого бара: {} Посадочных мест: {}".format(d,max(bar_seat))




def get_smallest_bar(filepath):
    data1 = load_data(filepath)
    for f in data1.get('features'):
        bar_seat.append(f.get('properties').get('Attributes').get('SeatsCount'))
    for f in data1.get('features'):
        if f.get('properties').get('Attributes').get('SeatsCount') == min(bar_seat):
            d = f.get('properties').get('Attributes').get('Name')
    return "Название самого маленького бара: {} Посадочных мест: {}".format(d, min(bar_seat))



def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    print(get_biggest_bar(filepath))
    print(get_smallest_bar(filepath))
