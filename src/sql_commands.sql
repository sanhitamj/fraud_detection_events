
-- From command line to setup database:

psql
CREATE DATABASE fraud;
\c fraud
CREATE TABLE events (Index SERIAL PRIMARY KEY, probability real, predict smallint,
  org_name text, name text, tot_payout real, risk_score real, json text);



-- example
-- Python commands to manipulate postgresql database:
import psycopg2

#Write prediction and JSON string to database
conn = psycopg2.connect(dbname = 'fraud', port=5432, password='', user='wallace', host='localhost')
cur = conn.cursor()
cur.execute("INSERT INTO events (predict, json) VALUES (%s, %s)",(predict, json_ex))
conn.commit()
cur.close()
conn.close()


#Read table and print results
conn = psycopg2.connect(dbname = 'fraud', port=5432, password='', user='wallace', host='localhost')
cur = conn.cursor()
query = '''SELECT * FROM events;'''
cur.execute(query)
rows = cur.fetchall()
for i in xrange(len(rows)):
    print rows[i]
    print
cur.close()
conn.close()
