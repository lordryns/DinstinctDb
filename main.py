from fastapi import FastAPI 
from pydantic import BaseModel
import json, uuid
from typing import Union

app = FastAPI()

class DataModel(BaseModel):
    db_key: str
    title: str
    value: str
    data_type: Union["str", "int", "bool", "float"]

@app.get("/")
def home():
    return {"title": "DistinctDB"}


@app.post("/")
def home():
    return {"title": "DistinctDB"}


@app.post("/create_db")
async def create_db():
    key = str(uuid.uuid4())
    
    with open(f"db/db{key}.json", 'w') as fp:
        fp.write("{}")
    
    return  {
        "message": f"Database created successfully, keep your Key safe!",
        "key": key, 
        "success": True
    }


@app.post("/add_data")
async def add_data(key_model: DataModel):
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


@app.get("/get_data/{key}")
async def get_data(key: str):
    try:
        with open(f"db/db{key}.json", 'r') as fp:
            json_db = json.load(fp)
            return {
                "message": "Database opened successfully!",
                "key": key, 
                "data": json_db,
                "success": True
            }

    except Exception as e:
        return {
                "message": f"Unable to open database!  Raw error: {e}",
                "key": "Invalid key!", 
                "data": {}, 
                "success": False
        }



