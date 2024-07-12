from fastapi import FastAPI 
from pydantic import BaseModel
import json 

app = FastAPI()



@app.get("/")
def home():
    return {"title": "DistinctDB"}

@app.post("/create_db")
def create_db(key: str):
    with open(f"db/db{key}.json") as fp:
        fp.write("{}")
