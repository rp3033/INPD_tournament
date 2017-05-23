#!/usr/bin/env python
# tournament.py
# Robert Personette   Final Project #5
#  May 23 2017    v 1.3


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
	pname = name.replace("'", r"''")  #Find any quotes and reformate
        sql = "INSERT INTO player(name) VALUES (%s);"
        data = (pname, )
        cur.execute(sql,data)
        conn.commit()
        conn.close()      
    except Exception as e:
        print "registerPlayer : Exception =", e


def deleteMatches():		 
    """Remove all the match records from the database. TEST 1"""
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE match CASCADE;") 
        conn.commit()
        conn.close()
    except Exception as e:
        print "deleteMatches: Exception =", e


def deletePlayers():  
    """Remove all the players and playerstats records from the database."""
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE player CASCADE;") 
        conn.commit()
        conn.close()
    except Exception as e:
        print "deletePlayerss: Exception =", e


def countPlayers():    
    """Returns the number of players currently registered."""
    try:	
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) AS pcount FROM player;")
        pcount = cur.fetchall()[0][0]
        conn.commit()
        conn.close()
        return pcount
    except Exception as e:
        print "countPlayers: Exception =", e


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        sql = ("INSERT INTO match (winner_id,loser_id) VALUES(%s,%s);")
        data = (winnerID, loserID)
        cur.execute(sql, data)
        conn.commit()
        conn.close()
    except Exception as e:
        print "reportMatch: Exception =", e


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
        sql ="SELECT * FROM comp_standings;"          #select from view player, wins, matches
        cur.execute(sql)
        ps = cur.fetchall()
        conn.close()
        return ps
    except Exception as e:
	print "playerStandings Exception =", e 


def even(x):
    """test if player count is odd or even  """
    num = int(x)
    mod = num % 2
    if mod > 0:
       return 1    # odd number
    else:
       return 0    # even number	


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    i = 0                              #index
    pairs = []                         #storage to return paired players
    pcount = countPlayers()            #get number of playrs
    ps = playerStandings()             #get sorted list of players by wins
    if even(pcount) == 0:              #Even number of players
        for row in ps:                 #interate thru ordered list of players
            player1 = ps[i]            #index first player
            player2 = ps[i+1]          #index (paired)second player
                       #  player1 id player1 name,player2 id  player 2 name
            pairs.append((player1[0], player1[1], player2[0], player2[1])) #write players to pairs[]
            i+=2                       #increment by two to access player 2
	    if (i == pcount):          #0 relative, i=count is end of sorted list, return paired players
                return pairs
    else:
        raise ValueError("Tournament needs even number of players")

