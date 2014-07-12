from db import *
import csv

def import_schools(db, filename):
    f = open(filename, 'rb')
    cur = db.cursor()
    #f.readline() # consume header
    for line in csv.reader(f):
        print line
        cur.execute("insert into schools (name, address, Suburb, Sector, location) values (%s, %s, %s, %s, ST_PointFromText(%s))", line)
    f.close()

db = DB()
import_schools(db, "~/ACT_School_Locations.csv")
db.close()