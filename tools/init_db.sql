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

create table hospitals (id serial primary key, name text, location geometry(point));

CREATE FUNCTION school_distance(geometry) RETURNS float as $$
    select ST_Distance(location, ST_Centroid($1)) as d from schools order by d asc limit 1;
$$ LANGUAGE SQL;

CREATE FUNCTION hospital_distance(geometry) RETURNS float as $$
    select ST_Distance(location, ST_Centroid($1)) as d from hospitals order by d asc limit 1;
$$ LANGUAGE SQL;

insert into hospitals (name, location) values
    ('Canberra Hospital & Health Services', 'POINT(149.100637 -35.345912)'),
    ('Calvary Public Hospital', 'POINT(149.086731 -35.253254)'),
    ('QEII Family Centre', 'POINT(149.079181 -35.323296)');