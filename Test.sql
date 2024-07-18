-- CREATE DATABASE IF NOT EXISTS paises; -- single line comment
/*
2 lines or more
comment
*/
-- DROP DATABASE IF EXISTS paises;


-- SHOW DATABASES;

-- USE paises;

CREATE TABLE IF NOT EXISTS continents(
continent_id INT,
NAME VARCHAR(255) NOT NULL AUTO_INCREMENT,
PRIMARY KEY (continent_id)
);

DROP TABLE IF EXISTS continents;

CREATE TABLE IF NOT EXISTS continents(
continent_id INT,
NAME VARCHAR(255)
);
alter table continents Add primary key(continent_id);
alter table continents drop primary key;
alter table continents modify column continent_id int auto_increment primary key;
alter table continents modify column name varchar(255) not null;

create table if not exists languages(
language_id INT AUTO_INCREMENT,
name VARCHAR(50) NOT NULL ,
PRIMARY KEY (language_id)
);

CREate table if not exists regions(
regions_id int auto_increment,
name varchar(100) not null,
continent_id int,
Primary key(region_id),
constraint fk_region_continents Foreign key(continent_id) References continents(continent_id)
);

