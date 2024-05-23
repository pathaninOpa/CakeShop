from pydantic import BaseModel
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
