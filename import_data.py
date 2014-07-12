from db import *
import csv

def import_schools(db, filename):
    f = open(filename, 'rb')
    cur = db.cursor()
    f.readline() # consume header
    cur.execute("begin")
    for line in csv.reader(f):
        print line
        coord = [float(p) for p in line[-1].strip('"').strip('(').strip(')').split(', ')]
        print coord	
        line[-1] = "(%f, %f)" % tuple(coord)
        cur.execute("insert into schools (name, address, Suburb, Sector, location) values (%s, %s, %s, %s, %s)", line)
    f.close()
    cur.execute("commit")

db = DB()
import_schools(db, "ACT_School_Locations.csv")
db.disconnect()
