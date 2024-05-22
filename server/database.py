from schemas import user
from pymongo.mongo_client import MongoClient

class MongoDatabase:
    def __init__(self, uri):
        self.uri = uri

    def __enter__(self):
        self.client = MongoClient(self.uri)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def connect(self):
        try:
            self.client.admin.command("ping")
            print("Successfully connected to MongoDB!")
            print("--> ", self.client.list_database_names())
        except Exception as e:
            print(f"Error: {e}")

def db_get_user_by_name(target_collection, name):
    try:
        target_document = target_collection.find_one({"name": name})
    except Exception as e:
        print(f"An error occurred while fetching the user: {e}")
        return None
    return target_document

def db_get_all_users(target_collection):
    users = []
    try:
        cursor = target_collection.find()
        for target_document in cursor:
            users.append(user.USER(**target_document))
    except Exception as e:
        print(f"An error occurred while fetching all users: {e}")
        return None
    return users

def db_create_user(target_collection, user_info):
    try:
        result = target_collection.insert_one(user_info)
    except Exception as e:
        print(f"An error occurred while creating the user: {e}")
        return None
    return user_info

def db_update_user(target_collection, name, email, password):
    try:
        target_collection.update_one(
            {"name": name},
            {"$set": {"email": email, "password": password}}
        )
        target_document = target_collection.find_one({"name": name})
    except Exception as e:
        print(f"An error occurred while updating the user: {e}")
        return None
    return target_document

def db_remove_user(target_collection, name):
    try:
        target_collection.delete_one({"name": name})
    except Exception as e:
        print(f"An error occurred while removing the user: {e}")
        return False
    return True