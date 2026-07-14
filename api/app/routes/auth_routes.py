from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.auth import RegisterSchema, loginSchema
from cors.db import get_db
from services.user import RegisterUser, loginUser

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.post("/register")
def register(user : RegisterSchema , db : Session = Depends(get_db)):
    return RegisterUser(db, user)


@router.post("/login")
def login(user : loginSchema, db : Session = Depends(get_db)):
    return loginUser(db, user)