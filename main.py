from fastapi import FastAPI 
from pydantic import BaseModel
import json, uuid

app = FastAPI()


@app.get("/")
def home():
    return {"title": "DistinctDB"}

@app.post("/create_db")
def create_db():
    key = str(uuid.uuid4())
    
    with open(f"db/db{key}.json", 'w') as fp:
        fp.write("{}")
    
    return  {
        "message": f"Database created successfully, keep your Key safe!",
        "key": key
    }


@app.post("/add_keys")
def add_keys():
    pass