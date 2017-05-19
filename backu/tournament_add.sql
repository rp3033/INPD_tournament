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

-- store game matches,with winner's id, loser's id and match number
CREATE TABLE match (match integer, winner_id serial references players(id), loser_id serial references players(id));

SELECT * FROM match;
INSERT INTO match (match, winner_id, loser_id) VALUES (1,1,2);
INSERT INTO match (match, winner_id, loser_id) VALUES (2,3,4);
INSERT INTO match (match, winner_id, loser_id) VALUES (3,5,6);
INSERT INTO match (match, winner_id, loser_id) VALUES (4,7,8);
INSERT INTO match (match, winner_id, loser_id) VALUES (5,9,10);
INSERT INTO match (match, winner_id, loser_id) VALUES (6,11,12);
INSERT INTO match (match, winner_id, loser_id) VALUES (7,13,14);
INSERT INTO match (match, winner_id, loser_id) VALUES (8,15,16);
SELECT * FROM match;

SELECT * FROM players;
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Tom','Waits');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Billy','Bob');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Kat','Persone');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Burt','Backrack');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Himme','Lows');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'William','Jones') ;
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Estabon','Sanchez');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Brad','Hudson');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Pede','Bull');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Steve','Bierb');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Michael','Pers');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Maureen','Ryan');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Lisa','Moras');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Angelica','Gertchez');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Donald','Trump');
INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Rex','Tillerson');
SELECT * FROM players;

\d
\dt
