from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

#connection
def db_connect():
    db_name = "conf.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn

#index routing decorator
@app.route('/')
def show_index() -> 'html':
    return render_template('index.html')

#awards routing decorator
@app.route('/awards.html')
def awards():
    with db_connect() as db:
        cur = db.cursor()
        cur.execute(f'''SELECT * FROM nominees;''')
        nominees = cur.fetchall()

    return render_template('awards.html', nominees=nominees)

#activities routing decorator
@app.route('/activities.html')
def show_activities() -> 'html':
    return render_template('activities.html')

#meals routing decorator
@app.route('/meals.html')
def show_meals() -> 'html':
    return render_template('meals.html')

#keynote routing decorator
@app.route('/keynote.html')
def show_keynote() -> 'html':
    return render_template('keynote.html')

#workshopschedule routing decorator
@app.route('/workshopschedule.html')
def workshopschedule():
    with db_connect() as db:
        cur = db.cursor()
        cur.execute('''SELECT * FROM workshops;''')
        workshops = cur.fetchall()

    return render_template('workshopschedule.html', workshops=workshops)

#registration routing decorator
@app.route('/registration.html', methods=['GET'])
def show_registration() -> 'html':
    return render_template('registration.html')

#poll routing decorator
@app.route('/poll.html')
def show_poll() -> 'html':
    return render_template('poll.html')

#thankyou routing decorator
@app.route('/registration.html', methods=['POST'])
def show_thankyou() -> 'html':
    return render_template('thankyou.html')

#admin routing decorator
@app.route('/admin.html')
def show_admin() -> 'html':
    return render_template('admin.html')

#nametags8 routing decorator
@app.route('/nametags8gen.html')
def nametags8gen():
    with db_connect() as db:
        cur = db.cursor()
        cur.execute('''SELECT * FROM registrationtable;''')
        registrants = cur.fetchall()

        return render_template('nametags8gen.html', registrants=registrants)

#nametags10 routing decorator
@app.route('/nametags10gen.html')
def nametags10gen():
    with db_connect() as db:
        cur = db.cursor()
        cur.execute('''SELECT * FROM registrationtable;''')
        registrants = cur.fetchall()

        return render_template('nametags10gen.html', registrants=registrants)



if __name__ == '__main__':
    app.run()
