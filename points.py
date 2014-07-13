from db import *
import simplekml
import re

def to_point(str):
    m = re.match(r"POINT\((\S+) (\S+)\)", str)
    return (m.group(1), m.group(2))

def gen_schools_kml(db):
    cur = db.cursor()
    cur.execute("select name, ST_AsText(location) from schools");
    kml = simplekml.Kml()
    for row in cur:
        p = kml.newpoint(name=row[0], coords=[to_point(row[1])])
    return kml.kml()

def gen_hospitals_kml(db):
    cur = db.cursor()
    cur.execute("select name, ST_AsText(location) from hospitals");
    kml = simplekml.Kml()
    for row in cur:
        p = kml.newpoint(name=row[0], coords=[to_point(row[1])])
    return kml.kml()

point_kml_funcs = {'schools': gen_schools_kml,
                   'hospitals': gen_hospitals_kml}

def point_layer_kml(layer):
    db = DB()
    if layer in point_kml_funcs:
        result = point_kml_funcs[layer](db)
    else:
        raise Exception
    db.disconnect()
    return result

