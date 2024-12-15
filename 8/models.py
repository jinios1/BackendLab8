from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
