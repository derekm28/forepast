DROP DATABASE IF EXISTS forepast;
CREATE DATABASE forepast;
\connect forepast


-- DROP DATABASE IF EXISTS forepast_test;
-- CREATE DATABASE forepast_test;
-- \connect forepast_test

CREATE TABLE locations
(
    id INTEGER NOT NULL,
    city TEXT NOT NULL,
    type TEXT NOT NULL,
    timezone TEXT,
    woeid INTEGER NOT NULL
)
CREATE TABLE weather_info
(
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  applicable_date DATE NOT NULL,
  latt_long FLOAT,
  time DATETIME,
  wind_speed FLOAT,
  wind_direction TEXT,
  (min|max|the)_temp INTEGER
  air_pressure FLOAT,
  humidity FLOAT NOT NULL,
  visibility FLOAT,

);

-- INSERT INTO locations
--     (city, release_year, runtime, rating)
-- VALUES
