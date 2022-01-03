import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def mostLoyalCommenter(post_id):
    tmpl = '''
           SELECT u.first_name, u.last_name
           FROM USERS as u
           WHERE user_id = (
                SELECT user_id
                FROM COMMENT
                WHERE post_id = %s
                GROUP BY user_id
                ORDER BY count(user_id) DESC
                LIMIT 1)
           '''
    cmd = cur.mogrify(tmpl,(post_id,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['fname', 'lname'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Complex Query 7: As an Influencer, I want to see the first and last name of the person who comments the most on my post, as I want to determine my most loyal followers")
mostLoyalCommenter(1)