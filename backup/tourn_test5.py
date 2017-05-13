     
import psycopg2
import sys



def main():

    players_dictionary = {'Tom':'Waits','Billy':'Bob','Kat':'Persone','Burt':'Backrack',
		     'Himme':'Lows','William':'Jones','Estabon':'Sanchez','Brad':'Hudson',
                     'Pit':'Bull','Steve':'Bierbussee','Steve':'Bierbussee','Michael':'Perse',
                     'Maureen':'Ryan','Lisa':'Moras','Julie':'Kaplove','Angelica':'Gertchez',
                     'Donald':'Trump','Rex':'Tillerson'}
 
    conn = []
    first_name = []
    last_name = []
 

    try:
        conn = psycopg2.connect(dbname="tournament")
	print "conn =",conn
    	cur = conn.cursor()
        print "cur =",cur
        print players_dictionary

        # Iterate thru players_dictionary.items(), get first & last name and Insert into players
        # table
        for first_name, last_name in players_dictionary.items():
            print "first =",first_name,"last =",last_name  
 
            cur.execute("INSERT INTO players (id,first,last) VALUES (%s, %s, %s);",format(DEFAULT , first_name, last_name)) 

        cur.execute("SELECT * FROM players;")
        conn.commit()
        conn.close()

    except Exception as e:
    	print "Exception =",e	
	 
 
if __name__ == "__main__":
	main()
	
 
#print "Value : %s" %  players_dictionary.items()
