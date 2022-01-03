import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def createPost(post_id, user_id):
    tmpl = '''
           INSERT INTO POST
           VALUES (%s,%s);
           SELECT *
           FROM POST
           WHERE (post_id = %s)
           '''
    cmd = cur.mogrify(tmpl,(post_id, user_id, post_id))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['post_id', 'user_id'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Simple Query 1: As a Normal User, I want to post pictures of myself so that my friends and followers can see what I’m up to.")
createPost(15, 1)