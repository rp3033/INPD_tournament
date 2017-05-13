#!/usr/bin/env python
#

import psycopg2


def deleteMatches():		 
    """Remove all the match records from the database. TEST 1"""
    print "(2)deleteMatches:SELECT * FROM match" 
	
    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()  		
	cur.execute("TRUNCATE TABLE match CASCADE;")     			 	 
        conn.commit()
	conn.close()
    except Exception as e:
        print "deleteMatches: Exception =",e


def deletePlayers(cur,conn):  
    """Remove all the match records from the database. TEST 1"""

    print "(3)deletePlayers:SELECT  * FROM players" 

    try:
        conn = psycopg2.connect(dbname="tournament")
        cur = conn.cursor()             
        cur.execute("TRUNCATE TABLE match CASCADE;")                                     
        conn.commit()
        conn.close()
    except Exception as e:
        print "deleteMatches: Exception =",e


def countPlayers(cur):    
    """Returns the number of players currently registered."""

    print "(5)countPlayers:SELECT * FROM match"  
	
    conn = psycopg2.connect(dbname="tournament")
    cur = conn.cursor()      	
    cur.execute("SELECT count(*) from players;")
    cur.fetchone()				
    count = cur.rowcount  				
    conn.close()
    print "count= ",count
    return count
