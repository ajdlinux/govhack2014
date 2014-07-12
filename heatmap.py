import simplekml
from db import *
from abs_stat import *
import re

def parse_multipolygon(kml, db_poly):
    multipoly = kml.newmultigeometry()
    db_poly = db_poly[14:-2]
    for poly in db_poly.split('),('):
        points = [[int(d) for d in point.split(' ')] for point in poly.split(',')]
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
    d['add'] += ',MEASURE.TT,POUR.TOT'
    d['datasetid'] = 'ABS_CENSUS2011_B03'
    abs_data = abs_get(d)['series']
    pop_data = dict()
    for row in cur:
        pop_data[row[0]] = parse_multpolygon(kml, row[1])
    kml.save(filename)
