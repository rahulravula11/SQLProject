import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def totalMoney(user_id):
    tmpl = '''
            SELECT p.user_id, sum(mp.money_made)
            FROM Monetized_post as mp
            JOIN Post as p on p.post_id = mp.post_id
            WHERE p.user_id = %s
            GROUP BY p.user_id
            ORDER BY p.user_id
           '''
    cmd = cur.mogrify(tmpl,(user_id,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['user_id','total_money_made'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Simple Query 5 (Analytical): As a Monetized User, I want to access the users ID along with the total money made off their monetized post, so I can calculate my revenues easier")
totalMoney(9)