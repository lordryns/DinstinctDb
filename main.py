from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import uuid
from databases import Database
import sqlalchemy

DATABASE_URL = "sqlite:///./distinct.db"
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

db_table = sqlalchemy.Table(
    "databases",
    metadata,
    sqlalchemy.Column("key", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("data", sqlalchemy.JSON),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

class DataModel(BaseModel):
    db_key: str
    title: str
    value: Union[str, int, bool, float]

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def home():
    return {"title": "DistinctDB"}

@app.post("/create_db")
async def create_db():
    key = str(uuid.uuid4())
    query = db_table.insert().values(key=key, data={})
    await database.execute(query)
    return {
        "message": "Database created successfully, keep your Key safe!",
        "key": key,
        "success": True
    }

@app.post("/add_data")
async def add_data(key_model: DataModel):
    query = db_table.select().where(db_table.c.key == key_model.db_key)
    row = await database.fetch_one(query)

    if row:
        data = row["data"]
        data[key_model.title] = key_model.value
        update_query = db_table.update().where(db_table.c.key == key_model.db_key).values(data=data)
        await database.execute(update_query)
        return {
            "message": "Value added successfully!",
            "success": True
        }
    else:
        return {
            "message": "Database not found!",
            "success": False
        }

@app.get("/get_data/{key}")
async def get_data(key: str):
    query = db_table.select().where(db_table.c.key == key)
    row = await database.fetch_one(query)

    if row:
        return {
            "message": "Database opened successfully!",
            "key": key,
            "data": row["data"],
            "success": True
        }
    else:
        return {
            "message": "Unable to open database!",
            "key": "Invalid key!",
            "data": {},
            "success": False
        }