from models import user
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
##################################################
class MongoDB:
    def __init__(self, uri):
        self.uri = uri
        self.client = MongoClient(uri)
    def connectMongoDB(self,uri):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            print("--> ",self.client.list_database_names())
            return True
        except Exception as e:
            print(e)
##################################################

load_dotenv
uri =os.getenv("uri")
print("Error: no uri found in .env file") if (not uri) else print("fetched uri from .env")
mongodb = MongoDB(uri)
mongodb.connectMongoDB(uri)
targetDB = mongodb.client.Bakery
targetCollection = targetDB.USERINFO

def fetch_one_usrinfo(name):
    targetDocument =  targetCollection.find_one({"name":name})
    return targetDocument
def fetch_all_usrinfo():
    usrinfo = []
    cursor = targetCollection.find()
    for targetDocument in cursor:
        usrinfo.append(user.USER(**targetDocument))
    return usrinfo
def create_usrinfo(usrinfo):
    targetDocument = usrinfo
    result =  targetCollection.insert_one(targetDocument)
    return targetDocument

def update_usrinfo(name, email, password):
    targetCollection.update_one({"$set":{
        "name":name,
        "email":email,
        "password":password
        }})
    targetDocument =  targetCollection.find_one({"name":name})
    return targetDocument

def remove_usrinfo(name):
    targetCollection.delete_one({"name":name})
    return True