import psycopg2
import string
import sys

match_dictionary = {'Tom Waits','Billy Bob','Kat Persone','Burt Backrack',
     'Himme Lows','William Jones','Estabon Sanchez','Brad Hudson',
     'Pit Bull','Steve Bierbussee','Michael Scanlon','Michael Perse',
     'Maureen Ryan','Lisa Moras','Julie Kaplove','Angelica Gertchez',
     'Donald Trump','Rex Tillerson'}

def main():
    curG = []
    connG = []
 
    try:
        conn = psycopg2.connect(dbname="tournament")
        print "conn =",conn
        cur = conn.cursor()
        print "cur =",cur
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (1,51,50);")       #############################
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (1,52,53);")		## OMW Opponant Match Wins ##
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (1,54,55);")		##
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (1,56,57);")		#56 = 1   57 = 0
		
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (2,52,51);")		
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (2,55,56);")		#56 = 0
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (2,53,50);")		
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (2,57,54);")		#         57 = 1
		
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (3,52,55);")
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (3,56,51);")		#56 = 1   57 = 0  
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (3,53,57);")		
        cur.execute("INSERT INTO match (match,winner_id,loser_id) VALUES (3,54,50);")			
        #print "Starting loop"
        #row = cur.fetchone()
        #while row is not None:
        #    print ", ".join([str(c) for c in row])
        #    row = cur.fetchone()
			
        conn.commit()
        conn.close()

    except Exception as e:
        print "I am unable to connect to the database: Exception =",e
    
	return
	
if __name__ == "__main__":
        main()
