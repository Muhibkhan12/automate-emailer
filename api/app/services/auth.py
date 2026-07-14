from fastapi import FastAPI,Depends,HTTPException,Header
from jose import jwt
from datetime import datetime,timedelta,UTC
from cors.config import settings

def create_token(data : dict):
    payload = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRY
    )

    payload.update({"exp":expire})
    encoded_jwt = jwt.encode(
        payload,
        settings.SECRET_KEY,
        settings.ALGORITHAM
    )
    return encoded_jwt
    

def verify_token():
    pass