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
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def loginUser(db, credentials):

    db_user = db.query(User).filter(
        User.email == credentials.email
    ).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(
        credentials.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

def logout():
    pass