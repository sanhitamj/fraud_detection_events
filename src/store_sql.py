'''
Function to insert values into a PostgreSQL database
'''

import psycopg2

user = 'wallace'
db = 'fraud'

def insert_vals(prob, predict, json_str, user=user):
    #Write prediction and JSON string to database
    conn = psycopg2.connect(dbname = db, port=5432, password='', user=user, host='localhost')
    cur = conn.cursor()
    for pr, p, j in zip(prob, predict, [json_str]):
        cur.execute("INSERT INTO events (probability, predict, json) VALUES (%s, %s, %s)",(pr, p, j))
    conn.commit()
    cur.close()
    conn.close()


def read_vals(user=user):
    #Read all values in table and return row-wise entries
    conn = psycopg2.connect(dbname = db, port=5432, password='', user=user, host='localhost')
    cur = conn.cursor()
    query = '''SELECT * FROM events;'''
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
