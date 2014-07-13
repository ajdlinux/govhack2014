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

CREATE FUNCTION school_distance(geometry) RETURNS float as $$
    select ST_Distance(location, $1) as d from schools order by d asc limit 1;
$$ LANGUAGE SQL;