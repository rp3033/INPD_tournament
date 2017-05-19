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
CREATE TABLE player (id serial primary key, name text);

-- store each game's match, winners id and loser id 
CREATE TABLE match (match integer, winner_id integer,loser_id integer);


-- store each players statistics 
CREATE TABLE playerStats (player_id integer, name text, wins integer, matches integer);


CREATE VIEW myplayerStats AS SELECT * FROM playerStats;
\d
\dt
