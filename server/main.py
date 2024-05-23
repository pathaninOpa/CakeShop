from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
app = FastAPI()

from models import user
from lib.database import (
    fetch_one_usrinfo,
    fetch_all_usrinfo,
    create_usrinfo,
    update_usrinfo,
    remove_usrinfo,
    fetch_one_cake_name,
    fetch_all_cake_info,
    create_cake_info,
    update_cake_info,
    remove_cake_info
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:{}".format(8000), "http://localhost:{}".format(3000)],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["Root"])
def read_root() -> dict:
    return {"Message":"Successfully connected."}

@app.get("/api/users",tags=['Users'])
def db_get_AllUsrinfo() -> List[user.USER]:
    response =  fetch_all_usrinfo()
    return response

@app.get("/api/users{name}", response_model=user.USER,tags=['Users'])
def db_get_usrinfo_by_id(name) -> List[user.USER]:
    response = fetch_one_usrinfo(name)
    if response:
        return response
    raise HTTPException(404, f"There is no User item with this name: {name}")

@app.post("/api/users", response_model=user.USER, tags=['Users'])
def db_post_usrinfo(usrinfo: user.USER) -> List[user.USER]:
    response =  create_usrinfo(usrinfo.model_dump())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad HTTP Request")

@app.put("/api/users{name}/", response_model= user.USER,tags=['Users'])
def db_put_usrinfo(name: str, email: str, password: str) -> List[user.USER]:
    response =  update_usrinfo(name, email, password)
    if response:
        return response
    raise HTTPException(404, f"There is no User item with this name: {name}")

@app.delete("/api/users{name}",tags=['Users'])
def db_delete_usrinfo(name) -> List[user.USER]:
    response =  remove_usrinfo(name)
    if response:
        return "Successfully deleted User Info.."
    raise HTTPException(404,  f"There is no User item with this name: {name}")

########################################################

@app.get("/api/cakes",tags=['Cakes'])
def db_get_all_cake_info() -> List[user.CAKE]:
    response =  fetch_all_cake_info()
    return response

@app.get("/api/cakes{name}", response_model=user.CAKE,tags=['Cakes'])
def db_get_cake_info_by_id(name) -> List[user.CAKE]:
    response = fetch_one_cake_name(name)
    if response:
        return response
    raise HTTPException(404, f"There is no Cake with this name: {name}")

@app.post("/api/cakes", response_model=user.CAKE, tags=['Cakes'])
def db_post_cake_info(CakeInfo: user.CAKE) -> List[user.CAKE]:
    response =  create_cake_info(CakeInfo.model_dump())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad HTTP Request")

@app.put("/api/cakes{name}/", response_model= user.CAKE,tags=['Cakes'])
def db_update_cake_info(name: str, shortDescription: str, description: str, image: str, ingredients: list, recipe: str, stock: int) -> List[user.CAKE]:
    response =  update_cake_info(name, shortDescription, description, image, ingredients, recipe, stock)
    if response:
        return response
    raise HTTPException(404, f"There is no Cake with this name: {name}")

@app.delete("/api/cakes{name}",tags=['Cakes'])
def db_delete_cake_info(name) -> dict:
    response =  remove_cake_info(name)
    if response:
        return {"message":f"Successfully deleted Cake({name}) Info.."}
    raise HTTPException(404,  f"There is no Cake with this name: {name}")