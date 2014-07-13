#!/bin/sh

# should be run after the schools table is loaded in

shp2pgsql -c -D -I SA2_2011_AUST.shp sa2 > sa2.sql
psql postgresql://whereshouldi@localhost -f sa2.sql
psql postgresql://whereshouldi@localhost -c "alter table sa2 add column school_distance float;"
psql postgresql://whereshouldi@localhost -c "update sa2 set school_distance = school_distance(geom);"