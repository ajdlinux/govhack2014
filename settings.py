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

# settings.py - local settings

SERVER_HOSTNAME = "whereshouldi.donnellan.id.au"
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# Database details
DB_HOST         = 'localhost'
DB_PORT         = 5432
DB_DATABASE     = 'whereshouldi'
DB_USER         = 'whereshouldi'
DB_PASSWORD     = 'whereshouldi'

# ABS Data settings
ABS_CSV = True
ABS_CSV_PATH = 'data/DataPacks/ACT'
ABS_EXCLUSION = [
    899999499, # No usual address
    897979799, # Shipping
    801031032, # Kowen
    801021029, # Namadgi
    801041043, # Hall
]
