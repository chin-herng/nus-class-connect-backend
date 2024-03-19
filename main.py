import os
import pymongo
from auth import *
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()
HOST = os.getenv('HOST')

client = pymongo.MongoClient(HOST)
db = client["LOGIN"]

app = Flask(__name__)

@app.route("/signup", methods=['POST'])
def signup_flask():
    request_data = request.get_json()
    request.headers.add('Access-Control-Allow-Origin', '*')
    email = request_data['email']
    password = request_data['password']
    return signup(email, password)

@app.route("/login", methods=['POST'])
def login_flask():
    request_data = request.get_json()
    request.headers.add('Access-Control-Allow-Origin', '*')
    email = request_data['email']
    password = request_data['password']
    return login(email, password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969, debug=True)