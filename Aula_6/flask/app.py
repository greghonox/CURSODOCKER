import requests
from flask_mysqldb import MySQL
from flask import Flask, jsonify


app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdocker'

def request_random():
    return requests.get('https://randomuser.me/api')

@app.route('/', methods=['GET'])
def indx():
  cur = mysql.connection.cursor()
  cur.execute("select * from users;")
  result = cur.fetchall()
  cur.close()
  return jsonify(result)

@app.route('/random', methods=['GET'])
def random():
  result = request_random()
  return jsonify(result.json())

@app.route("/inserthost", methods=['POST'])
def inserthost():
  data = request_random().json()
  username = data['results'][0]['name']['first']
  email = data['results'][0]['email']
  version = data['info']['version']
  
  print(username, email, version)
  
  cur = mysql.connection.cursor()
  cur.execute("""INSERT INTO users(name,email,version) VALUES(%s,%s,%s)""", (username,email,version))
  mysql.connection.commit()
  cur.close()

  return username

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)