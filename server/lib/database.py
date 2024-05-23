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
CakeCollection = targetDB.cakes
OrderCollection = targetDB.orders

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

########################################################

def fetch_one_cake_name(name):
    CakeName =  CakeCollection.find_one({"name":name})
    return CakeName

def fetch_all_cake_info():
    All_cake_info = []
    cursor = CakeCollection.find()
    for CakeDocument in cursor:
        All_cake_info.append(user.CAKE(**CakeDocument))
    return All_cake_info

def create_cake_info(CakeInfo):
    CakeDocument = CakeInfo
    result =  CakeCollection.insert_one(CakeDocument)
    return CakeDocument

def update_cake_info(name, shortDescription, description, image, ingredients, recipe, stock):
    CakeCollection.update_one({"$set":{
        "name":name,
        "shortDescription":shortDescription,
        "description":description,
        "image":image,
        "ingredients":ingredients,
        "recipe":recipe,
        "stock":stock
        }})
    CakeDocument =  CakeCollection.find_one({"name":name})
    return CakeDocument

def remove_cake_info(name):
    CakeCollection.delete_one({"name":name})
    return True

########################################################

def create_order_info(OrderInfo):
    OrderDocument = OrderInfo
    result =  OrderCollection.insert_one(OrderDocument)
    return OrderDocument