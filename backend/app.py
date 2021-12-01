from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'

mysql = MySQL(app)

@app.route('/person', methods = ['POST'])
def index():
    if request.method == 'POST':
        person = request.form
        Firstname = person['firstname']
        Lastname = person['lastname']
        
    return render_template('insert.html')

@app.route('/persons', methods = ['GET'])
def index():
    return render_template('select.html')

if __name__ == '__main__':
    app.run()
