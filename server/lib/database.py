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

async def fetch_one_usrinfo(name):
    targetDocument = await targetCollection.find_one({"name":name})
    return targetDocument
async def fetch_all_usrinfo():
    usrinfo = []
    cursor = targetCollection.find({})
    async for targetDocument in cursor:
        usrinfo.append(user.USER(**targetDocument))
    return usrinfo
async def create_usrinfo(usrinfo):
    targetDocument = usrinfo
    result = await targetCollection.insert_one(targetDocument)
    return targetDocument

async def update_usrinfo(name, email, password):
    await targetCollection.update_one({"$set":{
        "name":name,
        "email":email,
        "password":password
        }})
    targetDocument = await targetCollection.find_one({"name":name})
    return targetDocument

async def remove_usrinfo(name):
    await targetCollection.delete_one({"name":name})
    return True