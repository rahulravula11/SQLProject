import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def ageDemographics(post_id):
    tmpl = '''
            SELECT DISTINCT(u.first_name), u.last_name, u.date_of_birth, u.ethnicity
            FROM COMMENT as c
            JOIN Users as u on u.user_id = c.user_id
            WHERE c.post_id = %s
           '''
    cmd = cur.mogrify(tmpl,(post_id,))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['fname','lname','DOB','ethnicity'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Complex Query 10 (New Functionality): As a Company, I want to see to see the demographics of people who comment on my post, so I can see what type of people view my post")
ageDemographics(1)