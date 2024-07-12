from fastapi import FastAPI 
from pydantic import BaseModel
import json 

app = FastAPI()


class NewDbModel(BaseModel):
    key: str

@app.get("/")
def home():
    return {"title": "DistinctDB"}

@app.post("/create_db")
def create_db(model: NewDbModel):
    with open(f"db/db{model.key}.json", 'w') as fp:
        fp.write("{}")
    
    return  {
        "message": f"Database created successfully, keep your Key safe!",
        "key": model.key
    }
