CREATE EXTENSION cube;
CREATE EXTENSION earthdistance;
CREATE EXTENSION postgis;
--CREATE EXTENSION postgis_topology;
--CREATE EXTENSION postgis_tiger_geocoder;

CREATE TABLE schools (
    id serial PRIMARY KEY,
    name text,
    address text,
    Suburb text,
    Sector text,
    location point
);