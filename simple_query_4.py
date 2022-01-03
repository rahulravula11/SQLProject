import psycopg2 as pg2
from prettytable import PrettyTable
import sys

con = pg2.connect(database = 'tp', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def passwordChange(user_id,password):
    tmpl = '''
           UPDATE USERS
           SET password = %s
           WHERE user_id = %s;
           SELECT *
           FROM USERS
           WHERE (user_id = %s)
           '''
    cmd = cur.mogrify(tmpl,(password,user_id,user_id))
    cur.execute(cmd)

    rows = cur.fetchall()
    table = PrettyTable(['user_id','date_created','password','first_name','last_name','date_of_birth', 'ethnicity'])
    for row in rows:
        table.add_row(row)
    print(table)

print("Simple Query 4: As a Normal User, I want to change my password on Instagram, so that when I forget it, I can still access my account")
passwordChange(1,"newpassword")