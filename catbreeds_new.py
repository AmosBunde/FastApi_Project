from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()


class Cat(BaseModel):
    id: UUID
    breed: str
    size: str
    energy: str
    shedding: str

CATS = []

@app.get("/")
async def read_all_cats():
    return CATS


@app.post("/")
async def create_cat(cat: Cat):
    CATS.append(cat)
    return cat