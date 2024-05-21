from pymongo.mongo_client import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

class MongoDB:
    def __init__(self, uri):
        self.uri = uri
        self.client = MongoClient(uri)
    def connectMongoDB(self,uri):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            db =self.client.get_database()
            return db
        except Exception as e:
            print(e)

if __name__ == "__main__":
    load_dotenv
    app = FastAPI
    uri =os.getenv("uri")
    mongodb = MongoDB(uri)
    db = mongodb.connectMongoDB(uri)