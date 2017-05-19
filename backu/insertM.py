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
	cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (52,3,3,0);")
	cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (55,3,2,6);")
        cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (56,3,2,5);")
        cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (57,3,2,4);")
        cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (51,3,1,5);")
        cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (53,3,1,5);")
        cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (54,3,1,4);")
        cur.execute("INSERT INTO playerstats (player_id,matches,wins,omw) VALUES (50,3,0,0);")
		
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
