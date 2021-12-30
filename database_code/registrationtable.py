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

    #conn.close()

con = db_connect()
#our cursor object
cur = con.cursor()

#create award workshops table
cur.execute('DROP TABLE registrationtable;')
registrants = open('registrant_data_simplified.csv', 'r')
lines = registrants.readlines()
registrants.close()
headings = lines[0].strip().replace('\'', '').split(',')
vals = []

registrant = {}
i = 0

for m, line in enumerate(lines):
    if(m>0):
        m = line.strip().replace('\'', "").split(',')
        registrant[i] = {'fname': m[2], 'lname': m[3], 'position': m[12], 'company': m[13], 'city': m[6], 'state': m[7]}

        vals.append(tuple(registrant[i].values()))

        i = i + 1




cur.execute(f'''CREATE TABLE registrationtable(id INTEGER PRIMARY KEY AUTOINCREMENT,
{headings[2]} TEXT,
{headings[3]} TEXT,
{headings[12]} TEXT,
{headings[13]} TEXT, 
{headings[6]} TEXT, 
{headings[7]} TEXT);''')

cur.executemany(f'''INSERT INTO registrationtable ({headings[2]}, {headings[3]}, {headings[12]}, {headings[13]}, {headings[6]}, {headings[7]}) VALUES(?,?,?,?,?,?); ''', vals)

con.commit()
con.close()