#! /usr/bin/env python

import sys
import insert_codes
import jsonify

'''
Just give CSV path as first argument and second as the Open Data Base Json file and this would insert in database.
'''

insert_codes.open_csv(sys.argv[1])
insert_codes.open_json(sys.argv[2])
insert_codes.dump_json()

jsonify.jsonify('final_json.json')