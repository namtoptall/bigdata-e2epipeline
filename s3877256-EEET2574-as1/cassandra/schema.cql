CREATE TABLE weatherreport (
  forecastdate TIMESTAMP,
  location TEXT,
  description TEXT,
  temp FLOAT,
  feels_like FLOAT,
  temp_min FLOAT,
  temp_max FLOAT,
  pressure FLOAT,
  humidity FLOAT,
  wind FLOAT,
  sunrise BIGINT,
  sunset BIGINT,
  PRIMARY KEY (location, forecastdate)
);

CREATE TABLE twitterdata (
  tweet_date TIMESTAMP,
  location TEXT,
  tweet TEXT,
  classification TEXT,
  PRIMARY KEY (location, tweet_date)
);

use kafkapipeline;
create table if not exists kafkapipeline.fakerdaata(
    name text, 
    address text, 
    phone text,
    job text,
    email text,
    copmany text,
    country text,

    primary key(name, adrress)
);


create table if not exists kafkapipeline.mockaroo(
id int,
first_name string,
last_name string,
name string,
age int,
primary key(id)
);




