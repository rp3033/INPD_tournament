#!/usr/bin/env python
# tournament2.py


import psycopg2


def main():
    
    
    deleteMatches()
    deletePlayers()
    #registerPlayer('Billy Bob')
    registerPlayer('Kat Persone')
    #registerPlayer('Burt Backrack')
    registerPlayer('Tom Waits')
    registerPlayer('Brad Hudson')
    registerPlayer('Steve Bierbussee')
    registerPlayer('Maureen Ryan')
    registerPlayer('Rex Tillerson')
    registerPlayer('Michael Scanlon')
    registerPlayer('Donald Trump')
    all_rows = playerStandings()
    print "all_rows =", all_rows



def registerPlayer(pname):     
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    id = 0
    name = []

    print "(4)registerPlayer pname =",pname

	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()      				
        cur.execute("INSERT INTO players(name) VALUES (%s);", (pname,))	    	        
        conn.commit()
        cur.execute("INSERT INTO playerstats(name, matches, wins) VALUES (%s, 0, 0);", (pname,))
        conn.commit()
        sql ="SELECT id, name FROM players WHERE name = '%s';"%pname
        print "(1)sql ",sql
        cur.execute(sql)

	for id, name in cur.fetchall():
	    print id, name
            sql="UPDATE playerstats SET player_id = %d, name = '%s' WHERE playerstats.name = '%s';" %(id,pname,pname)
	    print "(2) sql ",sql
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
    print "(1)playerStandings()"
    conn = psycopg2.connect(dbname="tournament")
    cur = conn.cursor()
    cur.execute("SELECT * FROM playerstats;")
    all_rows = cur.fetchall()
    conn.close()
    return all_rows


def deleteMatches():		 
    """Remove all the match records from the database. TEST 1"""
    print "(2)deleteMatches:SELECT * FROM match" 
	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()  		
        cur.execute("DELETE FROM match;")
        conn.commit()
	conn.close()
    except Exception as e:
        print "deleteMatches: Exception =",e


def deletePlayers():  
    """Remove all the players and playerstats records from the database."""

    print "(3)deletePlayers:SELECT  * FROM players" 

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

    print "(5)countPlayers:SELECT * FROM match"  
	
    conn = psycopg2.connect(dbname="tournament")
    cur = conn.cursor()      	
    cur.execute("SELECT * from players;")
    cur.fetchone()				
    count = cur.rowcount  				
    conn.close()
    print "count= ",count
    return count


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """
    conn = psycopg2.connect(dbname="tournament")
    cur = conn.cursor()	
    sql = ("INSERT INTO match (winner_id, loser_id) VALUES(%s, %s)"%(winnerID,loserID))   
    print "sql = "
    cur.execute(sql)
    sql = "UPDATE playerstats SET (match, wins) = ((matchs + 1), (wins + 1)) WHERE id = %s , (winner,))"
    cur.execute(sql)
    sql = "UPDATE standing SET matchs = (matchs+1) WHERE id = %s, (loser,))"
    cur.execute(sql)
    conn.commit()
    conn.close()


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
  	#parings = []
        #checklist = []
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor() 
        sql = "SELECT playerstats.player_id, playerstats.name,  myplayerstats.player_id, myplayerstats.name FROM playerstats, myplayerstats WHERE playerstats.wins = myplayerstats.wins AND playerstats.player_id <> myplayerstats.player_id;"
        cur.execute(sql)      
        res = cur.fetchall()
        return res[:len(res)/2]
    except Excetion as e:
        print "swissPairings: Exception =" ,e        



if __name__ == "__main__":
        main()
