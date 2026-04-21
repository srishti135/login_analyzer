import pymongo
import os
import certifi

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017/")

client = pymongo.MongoClient(MONGO_URL, tlsCAFile=certifi.where())
db = client["login_security"]
collection = db["flagged_users"]

db = client["login_security"]
collection = db["flagged_users"]
# Inserts a flagged user into MongoDB
def insert_flagged_user(username, reason):
    document = {"username": username, "reason": reason}
    collection.insert_one(document)
    # Returns all flagged users from MongoDB
def get_all_flagged():
    return list(collection.find({}, {"_id": 0}))
# Clears all flagged users from MongoDB
def clear_flagged_users():
    collection.delete_many({})
    # Deletes a specific user from MongoDB
def delete_flagged_user(username):
    collection.delete_one({"username": username})