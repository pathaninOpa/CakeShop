from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
from dotenv import load_dotenv
from pymongo.collection import Collection

from database import *

import config
from schemas import user

load_dotenv()

uri = os.getenv("URI")

app = FastAPI()
target_collection: Collection = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"localhost:{config.PORT}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    global target_collection
    with MongoDatabase(uri) as mongodb:
        mongodb.connect()
        target_db = mongodb.client.Bakery
        target_collection = target_db.USERINFO

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Successfully connected."}

@app.get("/users", response_model=List[user.USER], tags=["Users"])
async def get_all_users() -> List[user.USER]:
    return db_get_all_users(target_collection)

@app.post("/users", response_model=user.USER, tags=["Users"])
async def create_user(usrinfo: user.USER) -> user.USER:
    user = db_create_user(target_collection, usrinfo.model_dump())
    if not user:
        raise HTTPException(400, "Something went wrong / Bad HTTP Request")
    return user

@app.put("/users/{name}", response_model=user.USER, tags=["Users"])
async def update_user(name: str, usrinfo: user.USER) -> user.USER:
    user = db_update_user(target_collection, name, usrinfo.email, usrinfo.password)
    if not user:
        raise HTTPException(404, f"There is no user with this name: {name}")
    return user

@app.get("/users/{name}", response_model=user.USER, tags=["Users"])
async def get_user_by_name(name: str) -> user.USER:
    user = db_get_user_by_name(target_collection, name)
    if not user:
        raise HTTPException(404, f"There is no user with this name: {name}")
    return user

@app.delete("/users/{name}", tags=["Users"])
async def delete_user(name: str) -> dict:
    user = db_remove_user(target_collection, name)
    if not user:
        raise HTTPException(404, f"There is no User item with this name: {name}")
    return {"message": "Successfully deleted User Info.."}