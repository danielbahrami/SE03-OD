from flask import Flask, request, redirect, jsonify
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(host='db', user='root', password='', database='db', cursorclass=pymysql.cursors.DictCursor)

@app.route('/person', methods = ['POST'])
def person():
    person = request.form
    firstName = person['firstname']
    lastName = person['lastname']
    with connection.cursor() as cur:
        cur.execute("INSERT INTO persons (firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    connection.commit()
    return redirect("https://localhost/select.html", 200)

@app.route('/persons', methods = ['GET'])
def persons():
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM persons")
        persons = cur.fetchall()
    return jsonify(persons)

if __name__ == '__main__':
    app.run()
