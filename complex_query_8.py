import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def mostPopularPostsComments():
    tmpl = '''
            SELECT post_id, message
            FROM COMMENT
            WHERE post_id = (
                SELECT post_id
                FROM COMMENT
                GROUP BY post_id
                ORDER BY count(post_id) DESC
                LIMIT 1)
           '''
    cmd = cur.mogrify(tmpl,)
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['name', 'message'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Complex Query 8: As a Company, I want to see which posts have the most comments and their comments, so I can make similar posts to achieve more interaction")
mostPopularPostsComments()