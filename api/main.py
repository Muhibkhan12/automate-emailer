from fastapi import FastAPI
from pydantic import BaseModel
# from typing import List
from app.routes.auth_routes import router

app = FastAPI()

app.include_router(router)
@app.get("/")
def home():
    return {'name': 'Muhib Hussain Khan'}

@app.get("/about")
def about():
    return {"data" : "Software engineer"}
