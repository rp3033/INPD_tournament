

import psycopg2
import string

def main():
    connG = []
    curG = []

    try:
        connG = psycopg2.connect(dbname="tournament")
        curG = conn.cursor()        
        print "conn =",conn
    except Exception as e:
        print "I am unable to connect to the database: Exception =",e


    return

                                                                                                                                            
def get_num_of_rounds(number_of_players):
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


if __name__ == "__main__":
        main()

