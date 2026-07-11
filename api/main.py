from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/")
def home():
    return {'name': 'Muhib Hussain Khan'}

@app.get("/about")
def about():
    return {"data" : "Software engineer"}
