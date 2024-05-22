from pydantic import BaseModel
class USER(BaseModel):
    name: str
    email: str
    password: str
