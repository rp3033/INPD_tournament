-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
--
-- Robert Personette 
--
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament
-- Stores players name and creates a unique key player ID
CREATE TABLE player (id serial PRIMARY KEY, name text);

-- Store each game's match and who won and who lost 
CREATE TABLE match (match_id serial PRIMARY KEY, winner_id INT REFERENCES player(id), loser_id INT REFERENCES player(id));

--Create a View that calculates how many matches, wins and losses each player has
--- and used in swissParings() to select who plays who
CREATE OR REPLACE VIEW comp_standings AS
     SELECT comp.id, comp.name,
    (SELECT count(*) FROM match WHERE match.winner_id = comp.id) AS wins,
    (SELECT count(*) FROM match WHERE match.winner_id = comp.id or match.loser_id = comp.id) AS matches
FROM player as comp
  GROUP BY id
  ORDER BY wins DESC,
           matches ASC;

-----------------------------------------------------------------------------
--Harry's VIEW for playerStandings , used to test against my playerStandings
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
