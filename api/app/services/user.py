from fastapi import HTTPException,status
from app.models.user import User
from app.services.auth import create_token
from app.services.security import hash_password, verify_password

def RegisterUser(db, user):

    hashed_password = hash_password(user.password)

    new_user = User(
        name = user.name,
        email = user.email,
        password = hashed_password,
    )
    
    db.add(User)
    db.commit()
    db.refresh(new_user)

    return new_user


def loginUser(db, user):
    user = db.query(User).filter(User.email == user.email).first()
    if  not User:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Invalid Email or Password"
        )
    
    if not verify_password(user.password, User.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=" Invalid Password or email"
        )
    
    token = create_token(
        {
        "sub" : str(user.id),
        "email" :  user.email 
        }
    )

    return{
        "access_token" : token,
        "token_type" : "bearer"
    }

def logout():
    pass