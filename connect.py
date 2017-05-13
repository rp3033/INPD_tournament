import psycopg2
import string

number_of_players= 4


def main():

    

    rounds = get_num_of_rounds(number_of_players):
    print rounds

    return

                                                                                                                                            
def get_num_of_rounds(number_of_players):
	rounds = 0
	print "(6)get_num_of_rounds"
	
	if number_of_players < 5:
		rounds = 2
	elseif if number_of_players >4 && number_of_players < 9:
		rounds = 3
	elseif if number_of_players >8 && number_of_players < 17:	
		rounds = 4
	elseif if number_of_players >16 && number_of_players < 33:
	    rounds = 5
		
	return rounds	
~                                                                                         
~                                                                                         
~              



if __name__ == "__main__":
        main()

