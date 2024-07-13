from fastapi import FastAPI 
from pydantic import BaseModel
import json, uuid
from typing import Union

app = FastAPI()

class CreateKeyModel(BaseModel):
    db_key: str
    title: str
    value: str
    data_type: Union["str", "int", "bool", "float"]

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
        "key": key, 
        "success": True
    }


@app.post("/add_key")
def add_keys(key_model: CreateKeyModel):
    try: 
        with open(f"db/db{key_model.db_key}.json", 'r') as fp:
            json_db = json.load(fp)
            
        json_db[key_model.title] = key_model.value

        with open(f"db/db{key_model.db_key}.json", 'w') as fp:
            
            json.dump(json_db, fp, indent=4, skipkeys=True)

        return {
            "message": "Value added successfully!",

        "success": True
    }

    except Exception as e:
        return {
            "message": f"Database not found! raw error: {e}",

        "success": False
        }