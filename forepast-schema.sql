DROP DATABASE IF EXISTS forepast;
CREATE DATABASE forepast;
\connect forepast


-- DROP DATABASE IF EXISTS forepast_test;
-- CREATE DATABASE forepast_test;
-- \connect forepast_test

CREATE TABLE locations
(
    id INTEGER NOT NULL,
    woeid INTEGER NOT NULL
)
CREATE TABLE weather_info
(
  id INTEGER NOT NULL,
  city_name TEXT NOT NULL,
  city_type TEXT NOT NULL,
  applicable_date DATE NOT NULL,
  date_time DATETIME,
  wind_speed FLOAT,
  wind_direction TEXT,
  the_temp INTEGER,
  max_temp INTEGER,
  min_temp INTEGER,
  air_pressure FLOAT,
  humidity FLOAT NOT NULL,
  visibility FLOAT,
);

-- INSERT INTO locations
--     (city, release_year, runtime, rating)
-- VALUES
