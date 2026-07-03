from sqlalchemy import Table,Column,Integer,String,Float,Boolean,Unique
from cors.db import meta,engine

users = Table(
    'users',meta,
    Column('id',Integer, primary_key = True),
    Column('name', String, Nullable=False),
    Column('email', String, Unique),
    Column('password', String),
)
meta.create_all(engine)
conn = engine.connect()

@app.get('/delete_user')
def delete_user():
    return {"Message": "User deleted"}