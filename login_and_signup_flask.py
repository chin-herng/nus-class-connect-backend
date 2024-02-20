from flask import Flask, request
from login_and_signup import *

app = Flask(__name__)

@app.route("/signup", methods=['POST'])
def signup_flask():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    return signup(username, password), 200

@app.route("/login", methods=['POST'])
def login_flask():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    return login(username, password), 200