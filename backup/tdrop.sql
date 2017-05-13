--postgres=# \i tdrop.sql
--psql:tdrop.sql:1: ERROR:  cannot drop table players because other objects depend on it
--DETAIL:  table playerstats column playerid depends on type players
--table match column player1id depends on type players
--table match column player2id depends on type players
--table match column won depends on type players
--HINT:  Use DROP ... CASCADE to drop the dependent objects too.
--psql:tdrop.sql:2: ERROR:  cannot drop table playerstats because other objects depend on it
--DETAIL:  table match column tournamentid depends on type playerstats
--HINT:  Use DROP ... CASCADE to drop the dependent objects too.
--DROP TABLE
--postgres=# drop 
DROP DATABASE tournament;
\d
DROP TABLE players CASCADE;
DROP TABLE playerStats CASCADE;
DROP TABLE match CASCADE;
\d
