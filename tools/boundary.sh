#!/bin/sh

shp2pgsql -c -D -I SA2_2011_AUST.shp sa2 > sa2.sql
psql postgresql://whereshouldi@localhost -f sa2.sql