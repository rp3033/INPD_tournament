#!/usr/bin/env python
# tournament.py


import psycopg2


#def main():
    
    
#    deleteMatches()
#    deletePlayers()
    #registerPlayer('Billy Bob')
#    registerPlayer('Kat Persone')
    #registerPlayer('Burt Backrack')
#    registerPlayer('Tom Waits')
#    registerPlayer('Brad Hudson')
#    registerPlayer('Steve Bierbussee')
#    registerPlayer('Maureen Ryan')
#    registerPlayer('Rex Tillerson')
#    registerPlayer('Michael Scanlon')
#    registerPlayer('Donald Trump')
#    all_rows = playerStandings()
#    print "all_rows =", all_rows



def registerPlayer(name):     
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    print "(0) registerPlayer name =",name
	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        print name.replace("'", r"''")  # raw string used her

	pname = name.replace("'", r"''")  # raw string used her
        print "(1) registerPlayer pname =",pname
        sql = "INSERT INTO players(name) VALUES ('%s');"%(pname)

        #sql = "INSERT INTO players(name) VALUES ('%s');"%(pname)

        print "(2) registerPlayer ",sql	    	        
        cur.execute(sql)
        conn.commit()
        sql= "INSERT INTO playerstats(name, matches, wins) VALUES ('%s', %d, %d);" %(pname,0,0)
        print "(3) registerPlayer ",sql  
        cur.execute(sql)
        conn.commit()
        sql ="SELECT id, name FROM players WHERE name = '%s';"%pname
        print "(4) registerPlayer ",sql
        cur.execute(sql)
	for id, name in cur.fetchall():
	    print "(5) id, name",id, name
            sql="UPDATE playerstats SET player_id = %d, name = '%s' WHERE playerstats.name =  '%s';" %(id,pname,pname)
	    print "(6) sql ",sql
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
    try:  
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()
        sql = "SELECT * FROM playerstats;"
        print "(2)playerStandings()",sql
        cur.execute(sql)
        all_rows = cur.fetchall()
        print "(3)playerStandings",all_rows
        conn.close()
        return all_rows
    except Exception as e:
        print "playerStandings: Exception =",e



def deleteMatches():		 
    """Remove all the match records from the database. TEST 1"""
    print "(0)deleteMatches" 
	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()  		
        cur.execute("DELETE FROM match;")
        conn.commit()

        sql = "SELECT * FROM match;"
        print "(1) sql",sql
        cur.execute(sql)
        all_rows = cur.fetchall()
        print "(2)deleteMatches",all_rows
        conn.commit()

        sql = "SELECT * FROM playerstats WHERE matches = 1;"
        print "(3)deletematches()",sql
        cur.execute(sql)

        print "(3a) deleteMatches"
	for id, name, wins, matches in cur.fetchall():
            print "(4) wins, matches",wins, matches
	    sql = "UPDATE playerstats SET matches = %d, wins = %d WHERE player_id = %d;"%(0,0,id)
            print "(5) sql = ",sql
            cur.execute(sql)
            conn.commit()

    
        conn.close()
    except Exception as e:
        print "deleteMatches: Exception =",e


def deletePlayers():  
    """Remove all the players and playerstats records from the database."""

    #print "(3)deletePlayers:SELECT  * FROM players" 

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
    try:	
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()      	
        cur.execute("SELECT * from players;")
        cur.fetchone()
        count = cur.rowcount 
        print "count = ",count 				
        conn.close()
        return count
    except Exception as e:
        print "countPlayers: Exception =",e


def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.
    """
    print"reportMatch(winnerID, loserID)", winnerID, loserID
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()	
        sql = ("INSERT INTO match (winner_id, loser_id) VALUES(%d, %d);"%(winnerID,loserID))   
        print "(0) sql = ",sql
        cur.execute(sql)
        print "(1) reportMatch after cur.execute() sql= ", sql
        sql ="SELECT wins, matches FROM playerstats WHERE player_id = %d;"%(winnerID)
        print "(2)reportMatch SELECT sql", sql
        cur.execute(sql)
        for wins, matches in cur.fetchall():
            print "(3) wins, matches",wins, matches
            matches = matches + 1
            wins = wins + 1 
            print "(4) wins, matches",wins, matches
            #sql="UPDATE playerstats SET wins = %d, matches = %d WHERE player_id = %d;" %(wins,matches,winnerID)
	    sql = "UPDATE playerstats SET matches = %d, wins = %d WHERE player_id = %d;"%(matches,wins,winnerID)
            print "(5) sql = ",sql
            cur.execute(sql)
            conn.commit()
            print "(6) after cur.execute() sql ",sql
	    sql = "UPDATE match SET match = %d WHERE winner_id = %d;"%(matches,winnerID)
            print "(7) sql ",sql
            cur.execute(sql)
            conn.commit()
		
        #sql= "INSERT INTO playerstats(name, matches, wins) VALUES ('%s', %d, %d);" %(pname,1,0)
        #sql = "INSERT INTO players(name) VALUES ('%s');"%(pname)
	sql ="SELECT wins, matches FROM playerstats WHERE player_id = %d;"%(loserID)
        print "(8)reportMatch SELECT loser", sql
        cur.execute(sql)
        for wins, matches in cur.fetchall():
            print "(9)matches", matches
            matches = matches + 1
            #sql="UPDATE playerstats SET wins = %d, matches = %d WHERE player_id = %d;" %(wins,matches,winnerID)
	    sql = "UPDATE playerstats SET matches = %d WHERE player_id = %d;" %(matches,loserID)
            print "(10) sql=",sql
            cur.execute(sql)
            print "(11) after cur.execute() sql ",sql

            conn.commit()
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
    print "swissPairings"
    try:    
  	#parings = []
        #checklist = []
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor() 
        sql = "SELECT playerstats.player_id, playerstats.name,  myplayerstats.player_id, myplayerstats.name FROM playerstats, myplayerstats WHERE playerstats.wins = myplayerstats.wins AND playerstats.player_id <> myplayerstats.player_id;"

        cur.execute(sql)
        tuple = cur.fetchall()
        print "(0) tuple ",tuple
        print "*******************************************************************************" 
	#ow = len(tuple)/10
	row = len(tuple)
	return tuple[0:4]
    except Exception as e:
        print "swissPairings: Exception =" ,e        


#if __name__ == "__main__":
#       main()
