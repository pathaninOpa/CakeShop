from pydantic import BaseModel
from typing import List

class USER(BaseModel):
    name: str
    email: str
    password: str

    def model_dump(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

class CAKE(BaseModel):
    name: str
    shortDescription: str
    description: str
    image: str
    ingredients: List[str]
    recipe: str
    stock: int

    def model_dump(self):
        return {
            "name":self.name,
        "shortDescription":self.shortDescription,
        "description":self.description,
        "image":self.image,
        "ingredients":self.ingredients,
        "recipe":self.recipe,
        "stock":self.stock
        }

class ORDER(BaseModel):
    name: str
    UserName: str

    def model_dump(self):
        return {
            "name":self.name,
            "UserName":self.UserName,
        }
    
