from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

app = FastAPI()


class Cat(BaseModel):
    id: UUID
    breed: str = Field(min_length =1)
    size: str
    energy: str
    shedding: str
    description: Optional[str] = Field(breed = "Description of the cat",
                                       max_length= 100)

CATS = []

@app.get("/")
async def read_all_cats():
    return CATS


@app.post("/")
async def create_cat(cat: Cat):
    CATS.append(cat)
    return cat


def create_cat_no_api():
    cat_01 = Cat(id= "4c48bb44-ab5a-41dc-b9bc-3b7d4adcd6ce",
                  breed= "American Wirehair Cat Breed",
                  size="Small",
                  energy= "High",
                  shedding= "Heavy",
                  description= ""
                  )
     cat_02 = Cat(id= "e062f488-5619-4614-9f19-187eb3ba8e2f",
                  breed= "Chartreux Cat Breed",
                  size="Small",
                  energy= "Low",
                  shedding= "Minimal",
                  description= ""
                  )
     cat_03 = Cat(id= "700988a0-6b19-407a-af7c-299e0994490e",
                  breed= "Exotic Shorthair Cat Breed",
                  size="Small",
                  energy= "High Low",
                  shedding= "Heavy",
                  description= ""
                  )
     cat_04 = Cat(id= "fc0af698-bdf7-4ed6-aa84-93fde5652e3e",
                  breed= "Japanese Bobtail Cat Breed",
                  size="Small",
                  energy= "",
                  shedding= "Minimal",
                  description= ""
                  )

    CATS.append(cat_01)
    CATS.append(cat_02)
    CATS.append(cat_03)
    CATS.append(cat_04)
    