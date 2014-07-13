import simplekml
from db import *
from abs_stat import *
from settings import *
import re
import os

class ColourMap(object):
    def __init__(self, values):
        self.min = min(values.values())
        self.max = max(values.values())
        self.range = self.max - self.min
#        self.mincol = {'r' : 255, 'g' : 230, 'b' : 230}
#        self.maxcol = {'r' : 255, 'g' : 0, 'b' : 0}
        self.mincol = {'r' : 240, 'g' : 240, 'b' : 255}
        self.maxcol = {'r' : 0, 'g' : 0, 'b' : 255}

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
        colstring = "%02x%02x%02x%02x" % (self.a, col['b'], col['g'], col['r'])
        return colstring

def parse_multipolygon(kml, code, db_poly, score_data, colmap):
    multipoly = kml.newmultigeometry()
    multipoly.style.polystyle.color = colmap.get_value(score_data[code])
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

def gen_kml(db, sa2_values):
    kml = simplekml.Kml()
    # get boundary data
    cur = db.cursor()
    cur.execute("select sa2_main, ST_AsText(geom) from sa2 where sa2_main like '8%' order by sa2_main asc")
    # do stuff with it
    colmap = ColourMap(sa2_values)
    for row in cur:
        if row[1] is not None and int(row[0]) not in ABS_EXCLUSION:
            parse_multipolygon(kml, int(row[0]), row[1], sa2_values, colmap)
    return kml.kml()

def gen_kml_file(db, sa2_values, kml_filename):
    kml = simplekml.Kml()
    # get boundary data
    cur = db.cursor()
    cur.execute("select sa2_main, ST_AsText(geom) from sa2 where sa2_main like '8%' order by sa2_main asc")
    # do stuff with it
    colmap = ColourMap(sa2_values)
    for row in cur:
        if row[1] is not None:
            parse_multipolygon(kml, int(row[0]), row[1], sa2_values, colmap)
    kml.save(kml_filename)

def gen_all_kml(db, folder):
    for name,f in get_data_funcs():
        data = f()
        print "Got data for %s" % name
        gen_kml_file(db, data, os.path.join(folder, name + '.kml'))
        print "Finished %s" % name

#db = DB()
#gen_all_kml(db, "assets")
#db.close()
