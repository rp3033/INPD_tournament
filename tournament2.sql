-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
-- Robert Personette 
--
--CREATE DATABASE tournament and create user root,  Only perform once ;
DROP DATABASE IF EXISTS tournament2;
CREATE DATABASE tournament;
\c tournament
\d
-- players defines the player's first last name and unique id
CREATE TABLE player (id serial PRIMARY KEY, name text);

-- store each game's match, winners id and loser id 
--CREATE TABLE match (match integer, winner_id integer,loser_id integer);
CREATE TABLE match (match_id INT, winner_id INT REFERENCES player(id), loser_id INT REFERENCES player(id));

--Create view to 
CREATE OR REPLACE VIEW comp_standings AS
     SELECT comp.id, comp.name,
    (SELECT count(*) FROM match WHERE match.winner_id = comp.id) AS wins,
    (SELECT count(*) FROM match WHERE match.winner_id = comp.id or match.loser_id = comp.id) AS matches
    FROM player as comp
    GROUP BY id
    ORDER BY wins DESC,
           matches ASC;


CREATE OR REPLACE VIEW current_standings AS
SELECT  id,
         name,
         SUM(CASE WHEN player.id = match.winner_id THEN 1 ELSE 0 END) AS wins,
         COUNT(match) AS match_count
FROM player
LEFT JOIN match
  ON player.id = match.winner_id OR player.id = match.loser_id
  GROUP BY id
  ORDER BY wins DESC,
           match_count ASC;

--\ds
--\dt
