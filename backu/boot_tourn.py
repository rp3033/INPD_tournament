import psycopg2

conn = psycopg2.connect(dbname="tournament")
cur = conn.cursor()
