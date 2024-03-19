import os
import pymongo
from auth import *
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()
HOST = os.getenv('HOST')

client = pymongo.MongoClient(HOST)
db = client["LOGIN"]

app = Flask(__name__)
CORS(app)

@app.route("/signup", methods=['POST'])
def signup_flask():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    message, error_code = signup(email, password)
    response = jsonify({
        'message': message,
        'error_code': error_code
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/login", methods=['POST'])
def login_flask():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    message, error_code = login(email, password)
    response = jsonify({
        'message': message,
        'error_code': error_code
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969, debug=True)