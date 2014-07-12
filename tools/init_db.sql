CREATE USER whereshouldi WITH PASSWORD 'whereshouldi';
CREATE DATABASE whereshouldi;
GRANT ALL PRIVILEGES ON DATABASE whereshouldi TO whereshouldi;

CREATE EXTENSION cube;
CREATE EXTENSION earthdistance;
CREATE EXTENSION postgis;
