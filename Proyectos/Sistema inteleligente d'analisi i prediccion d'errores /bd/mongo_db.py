#classe para moomgodb
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId

class MongoDB:
    def __init__(self, uri, database):
        self.uri = uri
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database]
            # Test the connection
            self.client.admin.command('ping')
            print("MongoDB connection successful.")
        except ConnectionFailure as e:
            print(f"MongoDB connection failed: {e}")

    def insert_data(self, collection_name, data):
        if self.db:
            collection = self.db[collection_name]
            result = collection.insert_one(data)
            print(f"Data inserted with id: {result.inserted_id}")
        else:
            print("Database not connected.")

    def find_data(self, collection_name, query):
        if self.db:
            collection = self.db[collection_name]
            result = collection.find(query)
            return list(result)
        else:
            print("Database not connected.")
            return None
        
    def update_data(self, collection_name, query, new_values):
        if self.db:
            collection = self.db[collection_name]
            result = collection.update_one(query, {'$set': new_values})
            print(f"Matched {result.matched_count} documents and modified {result.modified_count} documents.")
        else:
            print("Database not connected.")

    def delete_data(self, collection_name, query):  
        if self.db:
            collection = self.db[collection_name]
            result = collection.delete_one(query)
            print(f"Deleted {result.deleted_count} documents.")
        else:
            print("Database not connected.")

    def get_all_data(self, collection_name):
        if self.db:
            collection = self.db[collection_name]
            result = collection.find()
            return list(result)
        else:
            print("Database not connected.")
            return None
        
    def get_data_by_id(self, collection_name, object_id):
        if self.db:
            collection = self.db[collection_name]
            result = collection.find_one({"_id": ObjectId(object_id)})
            return result
        else:
            print("Database not connected.")
            return None
        
    def delete_all_data(self, collection_name):
        if self.db:
            collection = self.db[collection_name]
            result = collection.delete_many({})
            print(f"Deleted {result.deleted_count} documents.")
        else:
            print("Database not connected.")
            
    def close(self):
        if self.client:
            self.client.close()