# ImplementVim.py -- implementation of a Swiss-system tournament
#
# tourenament.sql  
#--CREATE DATABASE tournament and create user root,  Only perform once ;
#CREATE DATABASE  tournament;
#\c tournament;
#\d
#-- players defines the player's name and unique player id
#CREATE TABLE players (id serial primary key, name VARCHAR(20) NOT NULL);

#-- store game matches,with winner's id, loser's id and match number
#CREATE TABLE match (match integer, winner_id serial references players(id), loser_id serial references players(id));

#GRANT ALL PRIVILEGES ON TABLE players TO root;
#GRANT ALL PRIVILEGES ON TABLE playerstats TO root;
#GRANT ALL PRIVILEGES ON TABLE match TO root;

#-- a players running stats, ID, number of matches, number of wins
#CREATE TABLE playerStats (player_id serial references players(id), matches integer, wins integer);
######################################################################################

import psycopg2
import random
import string

players_dictionary = {'Tom Waits','Billy Bob','Kat Persone','Burt Backrack',
     'Himme Lows','William Jones','Estabon Sanchez','Brad Hudson',
     'Pit Bull','Steve Bierbussee','Steve Bierbussee','Michael Perse',
     'Maureen Ryan','Lisa Moras','Julie Kaplove','Angelica Gertchez',
     'Donald Trump','Rex Tillerson'}

match = 1
curG = []
connG = []    
     
	
 
def main():
    #SQL query commands needed to manipulate database records:
	#curG = []
    #connG = []   
#try:
#	 curG,connG = connect()					#connects fo tournament.standings
#	 deleteMatches(curG,connG)				#remove all the matches records from the database
#    deletePlayers(curG,connG)				#remove all the player records from the database
#    number_of_rows=countPlayers(curG)		#returns the number of players currently registred
#    for name in players_dictionary.items():	#while there's a name in players_dictionary register the players in tournament database
#        registerPlayer(name)                #adds a player to the tourenament database
	
#	number_of_players = countPlayers()		#Get number of players
#	rounds = get_num_of_rounds(number_of_players)	#Calulate number of rounds based on number of players
#	i = 0
#	while i <> rounds-1:					#while i doesn't equal rounds-1 (zero relative) play the max
#	    play_match()
#		i+=1								#bump match to next match+1
	
#	curG.execute("SELECT * FROM match;")	#Let ss
#	curG.execute("SELECT * FROM playerstats;")
#	connG.close()
#except Exception as e:
#    print "I am unable to connect to the database"	conn
#if __name__ == "__main__":
#	main()
############################################################ 


############################################################     

    def connect():				 
        """Connect to the PostgreSQL database.  Returns a database connection. TEST 1"""
 
        try:
            connG = psycopg2.connect(dbname="tournament")
            print "(1)connect:conn =",conn
            curG = conn.cursor()
            print "cur =",cur        
        except Exception as e:
	    print "connect: Exception =",e
            return 
	
    return cur,conn			#return psycopg2.connect("dbname=tournament")
 

########need commit() on line 93 #################### 
def deleteMatches():		#PASS TEST 1 
    """Remove all the match records from the database. TEST 1"""
	
    try:
        curG.execute("TRUNCATE TABLE match CASCADE;")  #TRUNCATE -- empty table match	    
	print "(2)deleteMatches:SELECT * FROM match"  
	curG.execute("SELECT * FROM match;")  	 
	match =+1
    except Exception as e:
        print "deleteMatches: Exception =",e


############################################################		
def deletePlayers(cur,conn):  #PASS TEST 1 
    """Remove all the match records from the database. TEST 1"""
	 
    curG.fetchall() 
    try:
        curG.execute("TRUNCATE TABLE players CASCADE;")	#TRUNCATE -- empty table players	    
	print "(3)deletePlayers:SELECT  * FROM players"       
	curG.execute("SELECT * FROM players;")        #verify table match is empty 	 	
    except Exception as e:
        print "deletePlayers: Exception =",e

		
############################################################
def registerPlayer(name):    #PASS TEST 1
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    print "(4)registerPlayer name =",name
	
    try:    
        #cur.execute("INSERT INTO players (name) VALUES (%s);", ('Tom Waits',))
	curG.execute("INSERT INTO players (name) VALUES (%s);", (name,))
        connG.commit() 		 
	curG.execute("SELECT * FROM players;")		#verify entry 
    except Exception as e:
        print "registerPlayer: Exception =",e

		
############################################################
def countPlayers(cur):   #PASS TEST 1  BUT number_of_row = 16L  or xxL to remove the L
    """Returns the number of players currently registered."""
    number_of_rows = 0	
    print "(5)countPlayers:SELECT * FROM match"  
	
    curG.execute("SELECT count(*) from players;") #Get number of rows
    result=cur.fetchone() #result holds tuple with one element, the value of COUNT(*)
    number_of_rows=result[0]	  #to find the number of rows
    print number_of_rows
    return number_of_row
	

############################################################	 
def get_num_of_rounds(number_of_players):	#PASS TEST 1
    rounds = 0
    print "(6)get_num_of_rounds"

    if number_of_players < 5:
        rounds = 2
    elif number_of_players >4 and number_of_players < 9:
        rounds = 3
    elif number_of_players >8 and number_of_players < 17:
        rounds = 4
    elif number_of_players >16 and number_of_players < 33:
        rounds = 5

    print "(6)get_num_of_rounds = ", rounds
    return rounds
	
	
def play_match():
    score1 = 0
    score2 = 0
    print "(7)get_num_of_rounds"
	
    id1, name1, id2, name2 = swissPairings()	#Get next set of players
    score1=roll_dice()							
    score2=roll_dice()
    winner_id, loser_id = get_winner(id1,score1,id2,score2)
    reportMatch(winner_id, loser_id)
    players_list = player_Standings()	#returns list of players and wins, sorted by most wins firt to least wins last_name
    match +=1
				
	
############################################################	
def roll_dice():		#PASS TEST 1
    """Roll the dice and returns the score but don't return a tie"""
    r1 = 0
    r2 = 0
    print "(8) roll_dice"  
	
    while (r1 == r2):
	r1 = random.randint(1,6)
	r2 = random.randint(1,6)
		
    print r1, r2
    return r1+r2
		
		
##############################################################
## play_game choose the higher score and records the match ###
##                                                         ###  
## input: id1 = player1, d1 = player1's dice score,        ###
##        id2 = player2, d2 = player2's dice score,        ### 
##                                                         ###
## returns: winner_id, loser_id                            ### 
############################################################## 
def get_winner(id1, d1, id2, d2):      #PASS TEST 1
     print "(9)role_dice"
		
     if (d1 > d2):
	report_match(id1, id2)        	
        return d1, d2
     elif (d2 > d1):
        report_match(id2, id1)
	return id2, id1
	    

def get_rank(tiedPAid, tiedPBid):
     """ Needed to rank players with same number of wins.  If you beat a player that has more wins than the
     player you tied with, than you rank higher and they rank lower. 	 
	 
	 OR When two players have the same numer of wins, use OMW  Opponant Match Wins to rank them
	 OMW is the total number of wins by players they have played against
	 Find the losing players in table match and count and return their Wins
	 """
	 
	#	return ranksHigh, ranksLow
 
		
def playerStandings(cur,coyerStandings):
   
#create a join of table players and match, by id to get name, id, wins, matches
#cur.execute("CREATE VIEW vw_player_stats AS SELECT * FROM players INNER JOIN match USING (id) ORDERED BY wins;")		 

    try:        	 
        print "(10)playerStandings"
        print "SELECT * FROM vw_player_stats ="
        curG.execute("SELECT * FROM vw_player_stats;")		#verify entry 
        connG.commit()        
        return vw_player_stats
    except Exception as e:
        print "playerStandings: Exception =",e
	
	

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    #conn = []
    #cur = []
    print "(11)report match winner = ",winner,"loser=",loser
	
    try:
	## record match winner_id & loser_id * match ##
        curG.execute("INSERT INTO match (match, winner_id, loser_id) VALUES (%s, %s, %s);", (match, winner, loser))
		
	#get winners total_matches and total_wins)
	## record winner_id total matches players and total wins ##
	curG.execute("INSERT INTO playerstats (player_id, matches, wins) VALUES (%s, %s, %s);", (winner, total_matches+=1, total_wins+=1)	 
        print "SELECT * FROM match"
	cur.execute("SELECT * FROM match;")		        #verify entry 
	print "SELECT * FROM playerstats"
	curG.execute("SELECT * FROM playerstats;")		#verify entry 
	connG.commit()
    except Exception as e:
        print "reportMatch: Exception =",e
 
 
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
  print "(12)swissPairings"
		

if __name__ == "__main__":
        main()

