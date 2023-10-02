from pydantic import BaseModel

# User
class User(BaseModel):
    name: str
    email: str
    password:str