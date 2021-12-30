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

#create workshops table
cur.execute('DROP TABLE workshops;')
workshops = open('workshops.csv', 'r')
lines = workshops.readlines()
workshops.close()
headings = lines[0].strip().replace('\'', '').split(',')
values = []

for m, line in enumerate(lines):
    if (m>0):
        m = line.strip().replace('\'', '').split(',')
        values.append(tuple(m))

cur.execute(f'''CREATE TABLE workshops(id INTEGER PRIMARY KEY AUTOINCREMENT,
{headings[0]} TEXT,
{headings[1]} TEXT,
{headings[2]} TEXT,
{headings[3]} TEXT, 
{headings[4]} TEXT, 
{headings[5]} TEXT, 
{headings[6]} TEXT, 
{headings[7]} TEXT, 
{headings[8]} TEXT, 
{headings[9]} TEXT, 
{headings[10]} TEXT, 
{headings[11]} TEXT, 
{headings[12]} TEXT);''')

cur.executemany(f'''INSERT INTO workshops ({headings[0]}, {headings[1]}, {headings[2]}, {headings[3]}, {headings[4]}, 
                {headings[5]}, {headings[6]}, {headings[7]}, {headings[8]}, {headings[9]}, {headings[10]}, {headings[11]}, {headings[12]}) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?); ''', values)

con.commit()
con.close()
