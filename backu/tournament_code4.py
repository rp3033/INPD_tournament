#! /usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import sys

def connect():
    print "connect"

    #DB = psycopg2.connect("dbname=tournament")
    #conn = psycopg2.connect("dbname=tournament") 
    #c = DB.cursor()
    #c.execute("SELECT * FROM players;")
    #DB.close()
    #return

connect()
print "done"

