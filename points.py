from db import *
import simplekml
import re

def to_point(str):
    m = re.match(r"POINT\((\S+) (\S+)\)", str)
    print m.groups()
    return (m.group(1), m.group(2))

def gen_schools_kml(db):
    cur = db.cursor()
    cur.execute("select name, ST_AsText(location) from schools");
    kml = simplekml.Kml()
    for row in cur:
        p = kml.newpoint(name=row[0], coords=[to_point(row[1])])
    return kml.kml()

point_kml_funcs = {'schools': gen_schools_kml}

def point_layer_kml(layer):
    if layer in point_kml_funcs:
        return point_kml_funcs[layer]()

#db = DB()
#f = open('schools.kml', 'w')
#f.write(gen_schools_kml(db))
#f.close()
#db.disconnect()
