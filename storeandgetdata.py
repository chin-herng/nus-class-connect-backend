from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://ahzong:GC8XEoqvQeDtjzRh@cluster0.jziurxd.mongodb.net/?retryWrites=true&w=majority')
db = client['LOGIN']

def store_data(user_id, data):
    # Create a document to store in the collection
    document = db.users.find_one({'user_id': user_id})
    document['data'] = data
    # Insert the document into the collection
    db.users.insert_one(document)

def retrieve_data(user_id):
    # Find the document with the given user ID
    document = db.users.find_one({'user_id': user_id})
    return document['data']


