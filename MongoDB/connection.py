from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://naman:naman123@cluster0.twv8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGODB_URL)

for db_name in client.list_database_names():
    print(db_name)