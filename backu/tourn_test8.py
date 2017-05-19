import psycopg2
import sys



def main():

    players_dictionary = {'Tom Waits','Billy Bob','Kat Persone','Burt Backrack',
		     'Himme Lows','William Jones','Estabon Sanchez','Brad Hudson',
                     'Pit Bull','Steve Bierbussee','Malcom Freckels','Michael Perse',
                     'Maureen Ryan','Lisa Moras','Julie Kaplove','Angelica Gertchez',
                     'Donald Trump','Rex Tillerson'}
 
    conn = []
    query = []

    try:
        conn = psycopg2.connect(dbname="tournament")
	print "conn =",conn
    	cur = conn.cursor()
        print "cur =",cur
        print players_dictionary

        # Insert an item
        # 
        for name in players_dictionary.items():
                print "name =",name  
		cur.execute("INSERT INTO players (name) VALUES (%S);", (name,))	
    		
        cur.execute("SELECT * FROM players;")
        conn.commit()
        conn.close()

    except Exception as e:
    	print "Exception =",e	
	 
 
if __name__ == "__main__":
	main()
	
		

 
#print "Value : %s" %  players_dictionary.items()
