from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    name : str
    email : EmailStr
    password : str
    email_verification : bool
    verification_token : str


class LoginSchema(BaseModel):
    email : EmailStr
    password : str
