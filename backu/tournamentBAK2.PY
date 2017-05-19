#!/usr/bin/env python
# tournament.py
### Robert Personette   Final Project #5

import psycopg2



     #registerPlayer('Julie Kaplove')
     #registerPlayer('Steve Bierbussee')
     #registerPlayer('Brad Hudson')
     #registerPlayer('Maureen Ryan')
     #registerPlayer('Lisa Moras')
     #registerPlayer('Rex Tillerson')
     #registerPlayer('Donald Trump')
     #registerPlayer('Tom Waits')
  
#    playerStandings()
#    swissPairings()
#    deletePlayers()


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
        #bname = bleach.clean(name, strip=true)
	pname = name.replace("'", r"''")  # raw string used her

        sql = "INSERT INTO player(name) VALUES (%s);"
        data = (pname, )
        cur.execute(sql,data)

        conn.commit()
        conn.close()      
    except Exception as e:
        print "registerPlayer : Exception =",e


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
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE player CASCADE;")     #TRUNCATE -- empty table players  d
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
        cur.execute("SELECT COUNT(*) AS pcount FROM player;")
        pcount = cur.fetchall()[0][0]
        conn.commit()
        conn.close()
        return pcount
    except Exception as e:
        print "countPlayers: Exception =",e


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """

    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        sql = ("INSERT INTO match (winner_id,loser_id) VALUES(%s,%s);")  
        data = (winnerID, loserID)
        cur.execute(sql,data)
        conn.commit()
        conn.close()
    except Exception as e:
        print "reportMatch: Exception =",e 


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
        sql ="SELECT * FROM comp_standings;"
        cur.execute(sql)
        ps = cur.fetchall()
        print "ps =",ps
        conn.close()
        return ps
    except Exception as e:
	print "playerStandings Exception =",e 


def even(x):

    print"x= ",x
    num = int(x)
    mod = num % 2
    print "mod= ",mod
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

    i = 0
    pairs = []
    pcount = countPlayers()
    ps = playerStandings()
    n = even(pcount)
    print "n =",n
    if even(pcount) == 0:              #Even number of players
        for row in ps:
            print "row =",row
            print "ps[",i,"]",ps[i] 
            player1 = ps[i]
            player2 = ps[i+1]
                       #  player1 id player1 name,player2 id  player 2 name  
            pairs.append((player1[0], player1[1], player2[0], player2[1]))
            print "pairs=",pairs
            i+=2
	    if (i == pcount):
                print "pairs = ",pairs
                return pairs
    else:
        #raise ValueError("Tournament needs even number of players")
        print "Tournament needs even number of players"

if __name__ == "__main__":
       main()

