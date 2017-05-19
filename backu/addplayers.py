#/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
#--CREATE DATABASE tournament and create user root,  Only perform once ;
#CREATE DATABASE  tournament;
#\c tournament;
#\d
#-- players defines the player's first last name and unique id
#CREATE TABLE players (id serial primary key, name text);

#-- a players running stats, ID, number of matches, number of wins
#CREATE TABLE playerStats (player_id serial references players(id), matches integer, wins integer);

#-- store game matches,with winner's id, loser's id and match number
#CREATE TABLE match (match integer, winner_id serial references players(id), loser_id serial referen$
#\d
#\dt

import psycopg2

def main():
    players_dictionary = {'Tom':'Waits','Billy':'Bob','Kat':'Persone','Burt':'Backrack',
                     'Himme':'Lows','William':'Jones','Estabon':'Sanchez','Brad':'Hudson',
                     'Pit':'Bull','Steve':'Bierbussee','Steve':'Bierbussee','Michael':'Perse',
                     'Maureen':'Ryan','Lisa':'Moras','Julie':'Kaplove','Angelica':'Gertchez',
                     'Donald':'Trump','Rex':'Tillerson'}

    conn = []
    first_name = []
    last_name = []

    try:
        conn = psycopg2.connect(dbname="tournament")
        print "conn =",conn
        cur = conn.cursor()
        print "cur =",cur
        print players_dictionary

        # Iterate thru players_dictionary.items(), get first & last name and Insert into players
        # table
        for first_name, last_name in players_dictionary.items():
            print "first =",first_name,"last =",last_name          

        #cur.execute("SELECT * FROM players;")
        conn.commit()
        conn.close()

    except Exception as e:
        print "Exception =",e


if __name__ == "__main__":
        main()


