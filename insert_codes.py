#! /usr/bin/env python

import csv
import json
import re
import sys

'''
First argument csv, second argument json to map
'''

csv_data = []
def open_csv(csv_path):
    global csv_data
    # f = open('/home/sanyam/GeekFest/csvdata.csv', 'rt')
    f = open(csv_path, 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            csv_data.append(row)
    finally:
        f.close()

data = {}
def open_json(json_path):
    # json_data = open('/home/sanyam/GeekFest/data.json').read()
    json_data = open(json_path).read()
    global data
    data = json.loads(json_data)
    for csv_list in csv_data:
        for i in range(len(data['data'])):
            if re.match(csv_list[2], data['data'][i][1], re.IGNORECASE):
                data['data'][i].insert(0, csv_list[0])
                data['data'][i].insert(1, csv_list[1])

def dump_json():
    final_data = {}
    for key, value in data.items():
        final_data[key] = value
    with open('final_json.json', 'w') as output_file:
        json.dump(final_data, output_file)

if __name__ == '__main__':
    open_csv(sys.argv[1])
    open_json(sys.argv[2])
    dump_json()