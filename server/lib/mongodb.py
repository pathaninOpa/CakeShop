from pymongo.mongo_client import MongoClient
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn
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

class User(BaseModel):
    name: str
    email: str
    password: str
##################################################

if __name__ == "__main__":
    load_dotenv
    app = FastAPI
    # uvicorn.run(app, host="localhost", port=8000)
    uri =os.getenv("uri")
    print("Error: no uri found in .env file") if (not uri) else print("fetched uri from .env")
    mongodb = MongoDB(uri)
    if (mongodb.connectMongoDB(uri)):
        targetDB =mongodb.client.Bakery
        targetCollection = targetDB.USERINFO
        targetCollection.insert_one({'name' : 'Nitiphoom'})
        print("  --> ",targetDB.list_collection_names())
        # @app.post("/api/register")
        # async def register(user: User):
        #     existing_user = targetDB.db.users.find_one({"email": user.email})
        #     if existing_user:
        #         raise HTTPException(status_code=400, detail="User with this email already exists")
        #     user_dict = user()
        #     targetDB.db.users.insert_one(user_dict)
        #     return JSONResponse(status_code=201, content={"message": "User registered successfully"})