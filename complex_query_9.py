import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def averageStoryInteractions(companyname):
    tmpl = '''
            SELECT c.company_name, avg(s.interaction_count)
            FROM Company as c
            JOIN Story as s on s.user_id = c.user_id
            WHERE c.company_name = %s
            GROUP BY c.user_id
           '''
    cmd = cur.mogrify(tmpl,(companyname,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['companyname', 'message'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Complex Query 9 (Analytical): As a Company, I want to see to see the average number of interactions of my stories, so I can see how many people interact with my stories")
averageStoryInteractions("Amazon")