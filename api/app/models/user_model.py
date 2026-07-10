from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name:str
    email:EmailStr
    password: str
    email_verified: bool
    verified_token: str
    