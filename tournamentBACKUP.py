#!/usr/bin/env python
# tournament.py
### Robert Personette   Final Project #5

import psycopg2

#ATE TABLE players CASCADE#
#    'Himme Lows','William Jones','Estabon Sanchez','Brad Hudson',
#    'Pit Bull','Steve Bierbussee','Steve Bierbussee','Michael Perse',
#    'Maureen Ryan','Lisa Moras','Julie Kaplove','Angelica Gertchez',
#    'Donald Trump','Rex Tillerson'}


match = 0


def main():

     registerPlayer('Julie Kaplove')
     registerPlayer('Steve Bierbussee')
     registerPlayer('Brad Hudson')
     registerPlayer('Maureen Ryan')
     registerPlayer('Lisa Moras')
     registerPlayer('Rex Tillerson')
     registerPlayer('Donald Trump')
     registerPlayer('Tom Waits')
  
     count =countPlayers()
     print "count ", count


 
     conn = psycopg2.connect(dbname="tournament")
     cur = conn.cursor()
 
     sql ="SELECT * from Player";
     print "(2) sql ", sql
     cur.execute(sql)
     all_rows = cur.fetchall()     
     print "(3) all rows ",all_rows
     conn.commit()
     conn.close()

#    deletePlayers()  

     conn = psycopg2.connect(dbname="tournament")
     cur = conn.cursor()
     sql ="SELECT * from Player";
     print "(4) sql ", sql
     cur.execute(sql)
     all_rows = cur.fetchall()     
     print "(5) all rows ",all_rows
     conn.commit()
     conn.close()



def registerPlayer(name):     
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    print "registerPlayer(name)", name	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
	pname = name.replace("'", r"''")  # raw string used her

        sql = "INSERT INTO player(name) VALUES (%s);"
        data = (pname, )
        cur.execute(sql,data)

        conn.commit()
        conn.close()      
    except Exception as e:
        print "registerPlayer : Exception =",e


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
 
   try:  
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        sql = "SELECT * FROM playerstats;"
        cur.execute(sql)
        all_rows = cur.fetchall()
        conn.close()
        return all_rows
    except Exception as e:
        print "playerStandings: Exception =",e


def deleteMatches():		 
    """Remove all the match records from the database. TEST 1"""
	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE match CASCADE;")     #TRUNCATE -- empty table matchs   
        conn.commit()
        conn.close()
    except Exception as e:
        print "deleteMatches: Exception =",e


def deletePlayers():  
    """Remove all the players and playerstats records from the database."""
    print "deletePlayers()"
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE player CASCADE;")     #TRUNCATE -- empty table players    
        conn.commit()
        conn.close()
    except Exception as e:
        print "deletePlayerss: Exception =",e


def countPlayers():    
    """Returns the number of players currently registered."""
    print "countPlayers"
    try:	
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()      	
        cur.execute("SELECT count(id) from player;")
        count = cur.fetchone()
        count[1:2]
        print "(1) count ",count
        conn.commit()
        conn.close()
        return count
    except Exception as e:
        print "countPlayers: Exception =",e


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """

    match +=1      #bump to next match
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()	
        sql = ("INSERT INTO match (match_id, winner_id, loser_id) VALUES(%s, %s, %s);")  
        data = (match, winnerID, loserID)
        cur.execute(sql,data)
        conn.commit()
        conn.close()
    except Exception as e:
        print "reportMatch: Exception =",e 


#def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    if c
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

#   try:    
#       conn = psycopg2.connect(dbname="tournament")
#       cur = conn.cursor() 
#       sql = "SELECT playerstats.player_id, playerstats.name,  myplayerstats.player_id, myplayerstats.name FROM playerstats, myplayerstats WHERE playerstats.wins = myplayerstats.wins AND playerstats.player_id <> myplayerstats.player_id;"

#       cur.execute(sql)
#       tuple = cur.fetchall()
#       return tuple[0:4]
#   except Exception as e:
#       print "swissPairings: Exception =" ,e        

if __name__ == "__main__":
       main()
