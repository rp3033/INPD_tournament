      
import psycopg2
import sys



def main():

    players_dictionary = {'Tom':'Waits','Billy':'Bob','Kat':'Persone','Burt':'Backrack',
		     'Himme':'Lows','William':'Jones','Estabon':'Sanchez','Brad':'Hudson',
                     'Pit':'Bull','Steve':'Bierbussee','Steve':'Bierbussee','Michael':'Perse',
                     'Maureen':'Ryan','Lisa':'Moras','Julie':'Kaplove','Angelica':'Gertchez',
                     'Donald':'Trump','Rex':'Tillerson'}
 
    conn = []
    query = []
    data = []

    try:
        conn = psycopg2.connect(dbname="tournament")
	print "conn =",conn
    	cur = conn.cursor()
        print "cur =",cur
        print players_dictionary

        # Iterate thru players_dictionary.items(), get first & last name and Insert into players
        # table
        for first, last in players_dictionary.items():
                print "first =",first,"last =",last  

                cur.execute("INSERT INTO players (first, last) VALUES ({0}, {1});".format(first, last))
        		

        cur.execute("SELECT * FROM players;")
        conn.commit()
        conn.close()

    except Exception as e:
    	print "Exception =",e	
	 
 
if __name__ == "__main__":
	main()
	
		

 
#print "Value : %s" %  players_dictionary.items()
