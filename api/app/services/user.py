from models.user import User
from services.security import hash_password

def RegisterUser(db, user ):

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
    user = db.query(User).all()
    
