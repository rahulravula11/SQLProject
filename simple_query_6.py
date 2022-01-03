import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def numPosts(user_id):
    tmpl = '''
            SELECT p.user_id, count(p.post_id)
            FROM Post as p
            WHERE user_id = %s
            GROUP BY p.user_id
            ORDER BY p.user_id
           '''
    cmd = cur.mogrify(tmpl,(user_id,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['user_id','num_posts'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Simple Query 6 (Analytical): As a User, I want to know how many posts I made, so I can keep an accurate count.")
numPosts(9)