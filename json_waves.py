#!/usr/bin/python

import sys
import json
import sqlite3

data = {}
#conn = sqlite3.connect("/home/ltratcliff/scripts/waves.db")
conn = sqlite3.connect("waves.db")
cur = conn.cursor()
sql = 'SELECT * from waves;'
cur.execute(sql)
results = cur.fetchall()
data['results'] = []
#test
data = []

for i in results:
    data.append({
            'date':i[0],
            'wind':i[1],
            'waves':i[2],
            'swell':i[3],
            'rain':i[4]
            })

print 'Content-Type: application/json\n\n'
print json.dumps(data)
