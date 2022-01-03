import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def moneyMade(post_id):
    tmpl = '''
           SELECT post_id, money_made
           FROM MONETIZED_POST
           WHERE (post_id = %s)
           '''
    cmd = cur.mogrify(tmpl,(post_id,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['post_id', 'money_made'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Simple Query 2: As a Monetized User or Company, I want to see how much money I made on my post, so I can track my revenue")
moneyMade(1)