from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from models import user
from lib.database import (
    fetch_one_usrinfo,
    fetch_all_usrinfo,
    create_usrinfo,
    update_usrinfo,
    remove_usrinfo
)
origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"dummy":"dummy"}

@app.get("/api/register")
def get_Allusrinfo():
    response =  fetch_all_usrinfo
    return response

@app.get("/api/register{name}", response_model=user.USER)
def get_usrinfo_by_id(name):
    response = fetch_one_usrinfo(name)
    if response:
        return response
    raise HTTPException(404, f"There is no User item with this name: {name}")

@app.post("/api/register")
def post_usrinfo(usrinfo: user.USER):
    response =  create_usrinfo(usrinfo.model_dump())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad HTTP Request")

@app.put("/api/register{name}/", response_model= user.USER)
def put_usrinfo(name: str, email: str, password: str):
    response =  update_usrinfo(name, email, password)
    if response:
        return response
    raise HTTPException(404, f"There is no User item with this name: {name}")

@app.delete("/api/register{name}")
def delete_usrinfo(name):
    response =  remove_usrinfo(name)
    if response:
        return "Successfully deleted User Info.."
    raise HTTPException(404,  f"There is no User item with this name: {name}")