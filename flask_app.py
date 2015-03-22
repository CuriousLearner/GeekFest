from flask import Flask, flash, render_template, session
import MySQLdb




app = Flask(__name__)
app.secret_key = 'lol'



@app.route('/')
def hello():
    return "Hello World"

@app.route('/data')
def show():
    db  = MySQLdb.connect(host="localhost",  user="root",passwd="root", db="CrimeData") 

    cur = db.cursor()

    cur.execute("SELECT *  FROM CRIME_STAT")

    for row in cur.fetchall():
        flash(row)

    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=True)
