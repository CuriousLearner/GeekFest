#! /usr/bin/env python

import json

def jsonify(final_json):
	# json_data = open('/home/sanyam/GeekFest/final_json.json').read()
	json_data = open(final_json).read()
	data = json.loads(json_data)
	files = open('final_indented_data.json', 'wb')
	files.write(json.dumps(data, indent=4))
	files.close()

if __name__ == '__main__':
	jsonify('final_json')