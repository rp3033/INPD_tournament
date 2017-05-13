import psycopg2
import random
import string

players_dictionary = {'Tom Waits','Billy Bob','Kat Persone','Burt Backrack',
     'Himme Lows','William Jones','Estabon Sanchez','Brad Hudson',
     'Pit Bull','Steve Bierbussee','Steve Bierbussee','Michael Perse',
     'Maureen Ryan','Lisa Moras','Julie Kaplove','Angelica Gertchez',
     'Donald Trump','Rex Tillerson'}

match = 0



def main():
    #SQL query commands needed to manipulate database records:
    curG = []
    connG = []   
 
    try:
        curG,connG = connect()					#connects fo tournament.standings
        deleteMatches(curG,connG)				#remove all the matches records from the database
        #deletePlayers(curG,connG)				#remove all the player records from the database
        #number_of_rows=countPlayers(curG)		#returns the number of players currently registered
        connG.commit() 
        connG.close()
    except Exception as e:
        print "I am unable to connect to the database"	
 
    return
	

def connect():
 """Connect to the PostgreSQL database.  Returns a database connection. TEST 1"""
 
    try:
        connG = psycopg2.connect(dbname="tournament")
        print "(1)connect:conn =",conn
        curG = conn.cursor()
        print "cur =",cur        
    except Exception as e:
        print "connect: Exception =",e

    return cur,conn			#return psycopg2.connect("dbname=tournament")

		
	
def deleteMatches(cur,conn):
    """Remove all the match records from the database. TEST 1"""
	
    try:
        curG.execute("TRUNCATE TABLE match CASCADE;") #TRUNCATE -- empty table match	    
        print "(2)deleteMatches:SELECT * FROM match"  
        curG.execute("SELECT * FROM match;")		     #verify table match is empty 		 
        match = match+1		
    except Exception as e:
        print "deleteMatches: Exception =",e
    
    return	

if __name__ == "__main__":
        main()

