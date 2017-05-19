#!/usr/bin/env python
# tournament.py
### Robert Personette   Final Project #5
###  May 19, 2017


import psycopg2

def main():

    deleteMatches()
    deletePlayers()



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
    print "deleteMatches"
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
    print "deletePlayers"

    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE player CASCADE;")     #TRUNCATE -- empty table players  d
        conn.commit()
        conn.close()
    except Exception as e:
        print "deletePlayers: Exception =",e


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
        print "countPlayers: Exception =",e


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """
    match +=1      #bump to next match
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        sql = ("INSERT INTO match (match_id,winner_id,loser_id) VALUES(%s,%s,%s);")  
        data = (match,winnerID, loserID)
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
        sql ="SELECT * FROM comp_standings;"     #from view get list of players sorted by wins
        cur.execute(sql)
        ps = cur.fetchall()
        conn.close()
        return ps
    except Exception as e:
	print "playerStandings Exception =",e 


def even(x):
    """Inputs an int and returns 1 if odd and 0 if even num"""
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
    pairs = []                         #stores returned pairs 	
    pcount = countPlayers()            #number of players  
    ps = playerStandings()             #get sorted list of players by wins in DB
    if even(pcount) == 0:              #if even number of players make pairs[]
        for row in ps:                 #iterate thru (DB) sorted list		
            player1 = ps[i]            #get first player		
            player2 = ps[i+1]          #get second player
                       ###player1 id  player1name player2 id  player 2 name  
            pairs.append((player1[0], player1[1], player2[0], player2[1]))
            i+=2                       #increment by two to get player2
	    if (i == pcount):          #0 relative list when i==count, i is out of range err  	
                print "pairs = ",pairs
                return pairs           #return list of paired players, paired by wins  
    else:
        raise ValueError("Tournament needs even number of players")



if __name__ == "__main__":
       main()

