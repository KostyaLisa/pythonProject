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
name VARCHAR(255) NOT NULL AUTO_INCREMENT,
PRIMARY KEY (continent_id)
);

DROP TABLE IF EXISTS continents;

CREATE TABLE IF NOT EXISTS continents(
continent_id INT,
name VARCHAR(255)
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

DROP TABLE IF EXISTS languages;

CREATE TABLE IF NOT EXISTS languages(
language_id INT,
name VARCHAR(50)
);
alter table languages Add primary key(language_id);
alter table languages drop primary key;
alter table languages modify column continent_id int auto_increment primary key;
alter table languages modify column name varchar(50) not null;
