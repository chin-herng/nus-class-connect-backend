# Sahej @thesahejagarwal
import pymongo
import re


client = pymongo.MongoClient("mongodb+srv://ahzong:GC8XEoqvQeDtjzRh@cluster0.jziurxd.mongodb.net/?retryWrites=true&w=majority")
db = client["LOGIN"]

def is_valid_email(email):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return email_pattern.match(email) is not None

def check_username(username):
    user = db.users.find_one({"username": username})
    return user is None and is_valid_email(username) 

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

INVALID_PASSWORD, INVALID_USERNAME = 1,2

def signup(username, password):
    if check_username(username):
      if check_password(password):
        user_data = {"username": username, "password": password}
        db.users.insert_one(user_data)
        return None
      else:
        return INVALID_PASSWORD
    return INVALID_USERNAME

def login(username, password):
    user = db.users.find_one({"username": username, "password": password})
    if user:
      return True
    return False