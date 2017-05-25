'''
Function to insert values into a PostgreSQL database
'''

import psycopg2

user = 'wallace'
db = 'fraud'


def insert_vals(prob=0, predict=0, org_name=' ', name=' ', tot_payout=0, risk_score=0, json_str=' ', user=user):
    #Write prediction and JSON string to database
    conn = psycopg2.connect(dbname = db, port=5432, password='', user=user, host='localhost')
    cur = conn.cursor()
    cur.execute("INSERT INTO events (probability, predict, org_name, name, tot_payout, risk_score, json_str) VALUES (%s, %s, %s, %s, %s, %s, %s)",(prob, predict, org_name, name, tot_payout, risk_score, json_str))
    conn.commit()
    cur.close()
    conn.close()


def read_vals(user=user):
    #Read all values in table and return row-wise entries
    conn = psycopg2.connect(dbname = db, port=5432, password='', user=user, host='localhost')
    cur = conn.cursor()
    query = '''SELECT DISTINCT risk_score, probability, predict, org_name, name, tot_payout FROM events ORDER BY risk_score DESC, probability DESC;'''
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
