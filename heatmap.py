import simplekml
from db import *
from abs_stat import *
import re

class colour_map:
    def __init__(self, values):
        self.min = min(values.values())
        self.max = max(values.values())
        self.range = self.max - self.min
        self.mincol = {'r' : 255, 'g' : 230, 'b' : 230}
        self.maxcol = {'r' : 255, 'g' : 0, 'b' : 0}
        self.a = 127
        
    def get_value(self, x):
        if x < self.min:
            col = self.mincol
        elif x > self.max:
            col = self.maxcol
        else:
            col = dict()
            for c in ('r', 'g', 'b'):
                col[c] = self.mincol[c] + (self.maxcol[c] - self.mincol[c]) * (x - self.min) / self.range
                col[c] = int(round(col[c]))
        print col
        colstring = "%02x%02x%02x%02x" % (self.a, col['g'], col['b'], col['r'])
        print colstring
        return colstring

def parse_multipolygon(kml, code, db_poly, abs_data, colmap):
    multipoly = kml.newmultigeometry()
    multipoly.style.polystyle.color = colmap.get_value(abs_data[code])
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
        kml_poly.outerboundaryis = points

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
    abs_dataj = abs_get(d)['series']
    abs_data = dict()
    for p in abs_dataj:
        abs_data[int(p['concepts'][4]["Value"])] = float(p['observations'][0]['Value'])
    print abs_data
    colmap = colour_map(abs_data)
    for row in cur:
        if row[1] is not None:
            parse_multipolygon(kml, int(row[0]), row[1], abs_data, colmap)
    kml.save(filename)

gen_pop_kml(DB(), 'assets/pop.kml')
