-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
 
--CREATE DATABASE tournament and create user root,  Only perform once ;
CREATE DATABASE  tournament;
\c tournament;
\d
-- players defines the player's first last name and unique id
CREATE TABLE players (id serial primary key, name text);

-- a players running stats, ID, number of matches, number of wins
CREATE TABLE playerStats (player_id serial references players(id), matches integer, wins integer);
CREATE TABLE players (id serial primary key, name VARCHAR(20) NOT NULL);

-- store game matches,with winner's id, loser's id and match number
CREATE TABLE match (match integer, winner_id serial references players(id), loser_id serial references players(id));

GRANT ALL PRIVILEGES ON TABLE players TO root;
GRANT ALL PRIVILEGES ON TABLE playerstats TO root;
GRANT ALL PRIVILEGES ON TABLE match TO root;

\d
\dt
