   
import psycopg2
import sys

### Read dictionary of players and insert into psql ###
#def insert_players():	 
#	 create_players_dictionay()
    
#    for first, last in players_dictionary.iteritems:
	 
#    cur.execute("INSERT INTO players (first, last) VALUES ({0}, {1};".format(first, last))
	 
#	 cur.execute("SELECT * FROM players;")


### Create a dictionary of players ###	 
#players_dictionary = '''{'Tom':'Waits','Billy':'Bob','Kat':'Persone','Burt':'Backrack','Himme':'Lows','William':'Jones','Estabon':'Sanchez','Brad':'Hudson','Pit':'Bull', 
#'Steve':'Bierbussee','Michael':'Perse','Maureen':'Ryan','Lisa':'Moras','Julie':'Kaplove','Angelica':'Gertchez','Donald':'Trump','Rex':'Tillerson'}'''
 

def main():


    players_dictionary = '''{'Tom':'Waits','Billy':'Bob','Kat':'Persone','Burt':'Backrack','Himme':'Lows','William':'Jones','Estabon':'Sanchez','Brad':'Hudson','Pit':'Bull', 
'Steve':'Bierbussee','Michael':'Perse','Maureen':'Ryan','Lisa':'Moras','Julie':'Kaplove','Angelica':'Gertchez','Donald':'Trump','Rex':'Tillerson'}'''
 
    conn = []

    try:
        conn = psycopg2.connect(dbname="tournament")
	print "conn =",conn
    	cur = conn.cursor()
        print "cur =",cur
        print players_dictionary

        # Insert an item
        # 
        for first, last in players_dictionary:
	        cur.execute("INSERT INTO players (first, last) VALUES ({0}, {1});".format(first, last))
		print "first =",first,"last =",last
		
        cur.execute("SELECT * FROM players;")
        conn.commit()
        conn.close()

    except Exception as e:
    	print "I am unable to connect to the database: Exception =",e	
	 
 
if __name__ == "__main__":
	main()
	
		

 
