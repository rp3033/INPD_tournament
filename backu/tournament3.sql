-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--CREATE DATABASE tournament and create user root,  Only perform once ;
CREATE DATABASE  tournament createuser root;
\c tournament;
\d
-- players defines the player's first last name and unique id
CREATE TABLE players (id text primary key, first text, last text);

-- a players running stats, ID, number of matches, number of wins
CREATE TABLE playerStats (player_id text references players(id), matches integer, wins integer);

-- store game matches,with winner's id, loser's id and match number
CREATE TABLE match (match integer, winner_id text references players(id), loser_id text references players(id));
\d
\dt
