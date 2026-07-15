from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schema.auth import RegisterSchema, LoginSchema
from app.cors.db import get_db
from app.services.user import RegisterUser, loginUser

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.post("/register")
def register(user : RegisterSchema , db : Session = Depends(get_db)):
    return RegisterUser(db, user)


@router.post("/login")
def login(user : LoginSchema, db : Session = Depends(get_db)):
    return loginUser(db, user)

@router.post("/logout")
def logout():
    return {
        "message" : "logged out successfully"
    }
