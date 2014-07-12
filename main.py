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

import bottle

import settings

@bottle.route('/')
@bottle.route('/index.html')
@bottle.view('index')
def index():
    return {'hostname': settings.SERVER_HOSTNAME}

@bottle.route('/about')
@bottle.view('about')
def about():
    return {}

@bottle.route('/contact')
@bottle.view('contact')
def contact():
    return {}

@bottle.route('/map')
@bottle.view('map')
def map():
    return {}

@bottle.route('/<path:path>')
def static(path):
    return bottle.static_file(path, root=os.path.join(os.path.dirname(__file__), 'assets'))

if __name__ == "__main__":
    # Make sure we're in the right directory!
    if os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(__file__))

    # Lights! Camera! ACTION!
    bottle.run(reloader=True, debug=True, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
