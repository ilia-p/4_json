import json
import pprint
import argparse

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with json')

def load_data(filepath):
    with open(filepath) as data_file:
        json_data = json.load(data_file)
    return json_data

def pretty_print_json(data):
    pprint.pprint(data)

if __name__ == '__main__':
    arg = parser.parse_args()
    json_data = load_data(arg.path)
    pretty_print_json(json_data)