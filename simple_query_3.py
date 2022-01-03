import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def deletePost(post_id):
    tmpl = '''
           DELETE FROM POST
           WHERE (post_id = %s);
           SELECT post_id, user_id
           FROM POST
           '''
    cmd = cur.mogrify(tmpl,(post_id,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['post_id', 'user_id'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Simple Query 3: As a Normal User, I want to delete a post that I made before because I no longer like it")
deletePost(12)