
import psycopg2
import string
import sys

players_dictionary = {'Tom Waits','Billy Bob','Kat Persone','Burt Backrack',
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
        #print players_dictionary
        cur.execute("SELECT * FROM players;")
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Tom Waits',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Billy Bob',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Kat Persone',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Burt Backrack',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Himme Lows',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Michael Scalon',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Estabon Sanchez',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Brad Hudson',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Burt Elmers',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Steve Bierbussee',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Donald Trump',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Julie Kaplove',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Lisa Moras',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Little Fatty',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('Kathy Scalon',))
        cur.execute("INSERT INTO players (name) VALUES (%s);", ('George Contras',))
        cur.execute("SELECT * FROM players;")    
		
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
