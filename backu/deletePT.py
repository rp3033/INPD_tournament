import psycopg2
import random
import string

players_dictionary = {'Tom Waits','Billy Bob','Kat Persone','Burt Backrack',
     'Himme Lows','William Jones','Estabon Sanchez','Brad Hudson',
     'Pit Bull','Steve Bierbussee','Steve Bierbussee','Michael Perse',
     'Maureen Ryan','Lisa Moras','Julie Kaplove','Angelica Gertchez',
     'Donald Trump','Rex Tillerson'}

match = 1
cur = []
conn = []

def main():
    #SQL query commands needed to manipulate database records:

    try:
       connect()					#connects fo tournament.standings
       deleteMatches()				#remove all the matches records from the database
       deletePlayers()				#remove all the player records from the database

       conn.commit()
       conn.close()
    except Exception as e:
       print "I am unable to connect to the database"	
	
def connect():
 """Connect to the PostgreSQL database.  Returns a database connection. TEST 1"""

try:
    conn = psycopg2.connect(dbname="tournament")
    print "(1)connect:conn =",conn
    cur = conn.cursor()
    print "cur =",cur        
except Exception as e:
    print "connect: Exception =",e

    
def deleteMatches():
    """Remove all the match records from the database. TEST 1"""
	
#try:
#    cur.execute("TRUNCATE TABLE match CASCADE;") #TRUNCATE -- empty table match	    
#    print "(2)deleteMatches:SELECT * FROM match"  
#    cur.execute("SELECT * FROM match;")		     #verify table match is empty 		 
#    match =+1		
#except Exception as e:
#    print "deleteMatches: Exception =",e
    
    	
	 
def deletePlayers():
    """Remove all the match records from the database. TEST 1"""

cur.execute("SELECT * FROM players;")
rows = cur.fetchall()	 
print "before deletePlayers()", rows

try:
    cur.execute("TRUNCATE TABLE players CASCADE;")	#TRUNCATE -- empty table players	    
    cur.execute("SELECT * FROM players;")        #verify table match is empty 	 	
    print "after deletePlayers()", rows
    rows = cur.fetchall()
    for row in cursor:
       print(row)

except Exception as e:
    print "deletePlayers: Exception =",e
	 
    
	
	
if __name__ == "__main__":
      main()
