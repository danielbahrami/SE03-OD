from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'

mysql = MySQL(app)

@app.route('/person', methods = ['POST'])
def person():
    if request.method == 'POST':
        person = request.form
        firstName = person['firstname']
        lastName = person['lastname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO persons (firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
    return render_template("insert.html")

@app.route('/persons', methods = ['GET'])
def persons():
    cur = mysql.connection.cursor()
    personsQuery = cur.execute("SELECT * FROM persons")
    if personsQuery > 0:
        persons = cur.fetchall()
    return render_template('select.html', data = persons)


if __name__ == '__main__':
    app.run()
