-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--CREATE DATABASE tournament;
CREATE DATABASE  tournament OWNER postgres;
\c tournament;
\d
CREATE TABLE players (playerID serial primary key, playerF text, playerL text);

CREATE TABLE playerStats (playerID players, matches integer, wins integer, tournamentID serial primary key);

CREATE TABLE match (tournamentID playerStats, match integer,player1ID players, player2ID players, won players);
\d
