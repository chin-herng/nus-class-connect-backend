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
    email = request_data['email']
    password = request_data['password']
    return signup(email, password), 200

@app.route("/login", methods=['POST'])
def login_flask():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    return login(email, password), 200

if __name__ == "__main__":
    app.run(debug=True)
    app.run()