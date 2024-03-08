import hashlib
import os
import pymongo
import re
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()
HOST = os.getenv('HOST')

client = pymongo.MongoClient(HOST)
db = client["LOGIN"]

app = Flask(__name__)

INVALID_EMAIL, INVALID_PASSWORD = 'invalid email', 'invalid password'

def is_valid_email(email):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return email_pattern.match(email) is not None

def check_email_exists(email):
    user = db.users.find_one({"email": email})
    return user is None

def check_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", password):
        return False
    return True

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()

def signup(email, password):
    if check_email_exists(email):
      if check_password(password):
        user_data = {"email": email, "password": hash_password(password)}
        db.users.insert_one(user_data)
        return 'successful'
      else:
        return INVALID_PASSWORD
    return INVALID_EMAIL

def login(email, password):
    user = db.users.find_one({"email": email, "password": password})
    if user:
      return 'successful'
    return 'invalid email or pasword'

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