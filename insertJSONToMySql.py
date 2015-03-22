import MySQLdb
import sys

import json
def insert(json_data):
    with open(json_data) as data_file :
        json_object = json.load(data_file)
        num_recs = len(json_object["data"])
        col_vals = []
        db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="CrimeData")
        print("DB connected")
        for i in range(num_recs):
            col_vals = []
            print("At record ",i,json_object["data"][i])
            if len(json_object['data'][i]) == 12:
                for j in range(12):
                    print("  -- > "+ str(i) + " : " + str(j) + " : "+ str(json_object["data"][i][j]))
                    col_vals.append(str(json_object["data"][i][j]))
                # modify INSERT_QUERY
                INSERT_QUERY = '''INSERT INTO CRIME_STAT VALUES (%s,%s,'%s','%s',%s,%s,%s,%s,%s,%s,%s,%s);''' % (tuple(col_vals))
                cur = db.cursor()
                cur.execute(INSERT_QUERY)
            else:
                pass
    db.commit()
    db.close()

if __name__ == '__main__':
    insert(sys.argv[1])
