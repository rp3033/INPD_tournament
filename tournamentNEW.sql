-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
-- Robert Personette 
--
--CREATE DATABASE tournament and create user root,  Only perform once ;
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament
\d
-- players defines the player's first last name and unique id
CREATE TABLE player (id serial PRIMARY KEY, name VARCHAR(255));

-- store each game's match, winners id and loser id 
--CREATE TABLE match (match integer, winner_id integer,loser_id integer);

CREATE TABLE match (match_id integer, winner_id int4 REFERENCES player(id), loser_id int4 REFERENCES player(id));

-- store each players statistics 
--CREATE TABLE playerStats (player_id integer, wins integer, matches integer);

CREATE TABLE playerStats (player_id int4 REFERENCES player(id), name VARCHAR(255),matches integer, wins integer);


--CREATE VIEW myplayerStats AS SELECT * FROM playerStats;
\d
\dt
