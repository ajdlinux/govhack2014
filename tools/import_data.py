from db import *

def import_schools(db, filename):
    f = open(filename, 'r')
    cur = db.cursor()
    for line in f:
        cols = line.split(',')
        cur.execute("insert into schools values (%s, %s, %s, %s, ST_PointFromText(%s))", cols)

db = DB()
import_schools(db, "~/ACT_School_Locations.csv")
db.close()