#!/usr/bin/env python
# tournament.py
### Robert Personette   Final Project #5

import psycopg2


def registerPlayer(name):     
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
	pname = name.replace("'", r"''")  # raw string used her
        sql = "INSERT INTO players(name) VALUES ('%s');"%(pname)
        cur.execute(sql)
        conn.commit()
        sql= "INSERT INTO playerstats(name, matches, wins) VALUES ('%s', %d, %d);" %(pname,0,0)
        cur.execute(sql)
        conn.commit()
        sql ="SELECT id, name FROM players WHERE name = '%s';"%pname
        cur.execute(sql)
	for id, name in cur.fetchall():
            sql="UPDATE playerstats SET player_id = %d, name = '%s' WHERE playerstats.name =  '%s';" %(id,pname,pname)
            cur.execute(sql)  
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
        cur.execute("DELETE FROM match;")
        conn.commit()
        sql = "SELECT * FROM match;"
        cur.execute(sql)
        all_rows = cur.fetchall()
        conn.commit()
        sql = "SELECT * FROM playerstats WHERE matches = 1;"
        cur.execute(sql)
	for id, name, wins, matches in cur.fetchall():
	    sql = "UPDATE playerstats SET matches = %d, wins = %d WHERE player_id = %d;"%(0,0,id)
            cur.execute(sql)
            conn.commit()
    
        conn.close()
    except Exception as e:
        print "deleteMatches: Exception =",e


def deletePlayers():  
    """Remove all the players and playerstats records from the database."""

    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("DELETE FROM players;")
        conn.commit()
        cur.execute("DELETE FROM playerstats;")
        conn.commit()
        conn.close()
    except Exception as e:
        print "deletePlayerss: Exception =",e


def countPlayers():    
    """Returns the number of players currently registered."""

    try:	
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()      	
        cur.execute("SELECT * from players;")
        cur.fetchone()
        count = cur.rowcount 
        conn.close()
        return count
    except Exception as e:
        print "countPlayers: Exception =",e


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """

    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()	
        sql = ("INSERT INTO match (winner_id, loser_id) VALUES(%d, %d);"%(winnerID,loserID))   
        cur.execute(sql)
        sql ="SELECT wins, matches FROM playerstats WHERE player_id = %d;"%(winnerID)
        cur.execute(sql)
        for wins, matches in cur.fetchall():
            matches = matches + 1
            wins = wins + 1 
	    sql = "UPDATE playerstats SET matches = %d, wins = %d WHERE player_id = %d;"%(matches,wins,winnerID)
            cur.execute(sql)
	    sql = "UPDATE match SET match = %d WHERE winner_id = %d;"%(matches,winnerID)
            cur.execute(sql)
		
	sql ="SELECT wins, matches FROM playerstats WHERE player_id = %d;"%(loserID)
        cur.execute(sql)
        for wins, matches in cur.fetchall():
            matches = matches + 1
	    sql = "UPDATE playerstats SET matches = %d WHERE player_id = %d;" %(matches,loserID)
            cur.execute(sql)
        conn.commit()
        conn.close()
    except Exception as e:
        print "reportMatch: Exception =",e 


def swissPairings():
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

    try:    
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor() 
        sql = "SELECT playerstats.player_id, playerstats.name,  myplayerstats.player_id, myplayerstats.name FROM playerstats, myplayerstats WHERE playerstats.wins = myplayerstats.wins AND playerstats.player_id <> myplayerstats.player_id;"

        cur.execute(sql)
        tuple = cur.fetchall()
	return tuple[0:4]
    except Exception as e:
        print "swissPairings: Exception =" ,e        

