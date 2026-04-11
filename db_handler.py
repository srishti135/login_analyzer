import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
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