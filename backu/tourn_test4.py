     
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

    try:
        conn = psycopg2.connect(dbname="tournament")
	print "conn =",conn
    	cur = conn.cursor()
        print "cur =",cur
        print players_dictionary

        # Insert an item
        # 
        for first, last in players_dictionary.items():
                print "first =",first,"last =",last  

                #cur.execute("INSERT INTO players (first, last) VALUES ({0}, {1});".format(first, last)
                #cur.execute("INSERT INTO PLAYERS (id, first, last) VALUES (DEFAULT, 'Rex','Tillerson');")

                #query = "INSERT INTO players (first, last) VALUES (%s,%s);"
		#data = (first, last)  
                #cur.execute(query,data)
                #query = "INSERT INTO players (first, last) VALUES (%s, %s);".format(first, last)
                #cur.execute(query,data)
    		
        cur.execute("SELECT * FROM players;")
        conn.commit()
        conn.close()

    except Exception as e:
    	print "Exception =",e	
	 
 
if __name__ == "__main__":
	main()
	
		

 
#print "Value : %s" %  players_dictionary.items()
