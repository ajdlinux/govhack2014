#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Where should I? - a tool to help you find where to do things!
Copyright © 2014 Andrew Donnellan, Teresa Bradbury, Suzette Bailey, Craig Thomler.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# main.py - main Bottle script

import sys
import os

from bottle import route, view, request, static_file, run

from settings import *
from abs_stat import data_funcs, get_scores
from heatmap import gen_kml
from points import point_layer_kml
from db import DB

@route('/')
@route('/index.html')
@view('index')
def index():
    return {'hostname': SERVER_HOSTNAME}

@route('/aboutus')
@view('aboutus')
def aboutus():
    return {}

@route('/contact')
@view('contact')
def contact():
    return {}

@route('/questions')
@view('questions')
def questions():
    return {}

@route('/map')
@view('map')
def map():
    return {}

@route('/heatmap.kml')
def heatmap():
    query = request.query.decode()
    params = []
    for param in data_funcs:
        try:
            params.append((param,
                           float(query[param + '_val']),
                           float(query[param + '_weight'])))
        except:
            pass
    # FIXME don't break when no params specified
    db = DB()
    kml = gen_kml(db, get_scores(params))
    db.disconnect()
    return kml


@route('/pointlayer.kml')
def pointlayer():
    return point_layer_kml(request.query.decode()['layer'])

@route('/<path:path>')
def static(path):
    return static_file(path, root=os.path.join(os.path.dirname(__file__), 'assets'))

if __name__ == "__main__":
    # Make sure we're in the right directory!
    if os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(__file__))

    # Lights! Camera! ACTION!
    run(reloader=True, debug=True, host=SERVER_HOST, port=SERVER_PORT)
