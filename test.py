import json
import pprint

with open('test.json') as data_file:
    json_data_list = [row for row in data_file]

for json_data in json_data_list:
    s = json.loads(json_data)
    pprint.pprint(s)

