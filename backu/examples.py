#! /usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
#import sys

conn = []

try:    
    conn = psycopg2.connect(dbname="tournament")
    cur = conn.cursor()

    # Insert an item
    # 

     print("Hello {0}, {1}".format("Bob",  "Rahul") )
     first_name = "Bob"
     last_name = "Robert"

     players_dict = {"Bob": "Robert", "Tom": "Waits"}
     
     for first_name, last_name in players_dict.iteritems: 
     cur.execute("INSERT INTO players (playerF, playerL) VALUES ({0}, {1});".format(first_name, last_name))
     conn.commit()
     conn.close()

except Exception as e:
    print "I am unable to connect to the database"
    print(e)

