import requests
from flask import request, json, jsonify, Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def indx():
    data = requests.get('https://randomuser.me/api')
    return data.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)