import simplekml
from db import *
from abs_stat import *
import re

def parse_multipolygon(kml, db_poly):
    multipoly = kml.newmultigeometry()
    db_poly = db_poly[14:-2]
    for poly in db_poly.split('),('):
        spoints = [point.split(' ') for point in poly.split(',')]
        points = []
        for p in spoints:
            if p[0].startswith('('):
                p[0] = p[0][1:]
            if p[1].endswith(')'):
                p[1] = p[1][:-1]
            points.append((float(p[0]), float(p[1])))
        kml_poly = multipoly.newpolygon()
        kml_poly.outboundaryis(points)

def gen_pop_kml(db, filename):
    kml = simplekml.Kml()
    # get boundary data
    cur = db.cursor()
    cur.execute("select sa2_main, ST_AsText(geom) from sa2 where sa2_main like '8%' order by sa2_main asc")
    
    # get population data
    d = dict()
    add_sa2(d)
    d['method'] = 'GetGenericData'
    d['and'] += ',MEASURE.TT,POUR.TOT'
    d['datasetid'] = 'ABS_CENSUS2011_B03'
    print d
    abs_data = abs_get(d)['series']
    print abs_data[0:4]
    pop_data = dict()
    for row in cur:
        if row is not None:
            pop_data[row[0]] = parse_multipolygon(kml, row[1])
    kml.save(filename)
