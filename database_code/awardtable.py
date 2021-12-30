import sqlite3

import ast


#creating our database connection
def db_connect():
    #name of the database
    db_name = "../conf.sqlite"
    #store connection in a variable
    conn = sqlite3.connect(db_name)
    #enables us to access data in a row
    conn.row_factory = sqlite3.Row
    #return the connection
    return conn



con = db_connect()
#our cursor object
cur = con.cursor()

#create award nominees table
cur.execute('DROP TABLE nominees;')
awardNominees = open('awards.csv', 'r')
lines = awardNominees.readlines()
awardNominees.close()
headings = lines[0].strip().replace('\'', '').split(',')

vals = []

for m, line in enumerate(lines):
    if(m>0):
        m = line.strip().replace('\'', "").split(',')
        vals.append(tuple(m))

cur.execute(f'''CREATE TABLE nominees(id INTEGER PRIMARY KEY AUTOINCREMENT,
{headings[0]} TEXT,
{headings[1]} TEXT,
{headings[2]} TEXT,
{headings[3]} INTEGER );''')

cur.executemany(f'''INSERT INTO nominees ({headings[0]}, {headings[1]}, {headings[2]}, {headings[3]}) VALUES(?,?,?,?); ''', vals)

con.commit()
con.close()

