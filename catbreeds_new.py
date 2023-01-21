from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from starlette.responses import JSONResponse


class NegativeNumberException(Exception):
    def __init__(self, cats_to_return):
        self.cats_to_return = cats_to_return




app = FastAPI()


class Cat(BaseModel):
    id: UUID
    breed: str = Field(min_length =1)
    size: str
    energy: str
    shedding: str
    description: Optional[str] = Field(breed = "Description of the cat",
                                       max_length= 100)


    rating: int = Field(gt= -2, lt= 101)


    class Config:
        schema_extra ={
            "example": {
                "id": "6940777b-3c69-4e1e-8732-34c14c0fb9bd",
                "breed": "Exotic Shorthair Cat Breed",
                "size": "Big",
                "energy": "High",
                "shedding": "Heavy"
            }
        }

class CatsWithoutRatings(BaseModel):
    id ; UUID
    breed: str = Field(min_length =1)
    size: str
    energy: str
    shedding: str
    description: Optional[str] = Field(breed = "Description of the cat",
                                       max_length= 100)



CATS = []

@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request, exception: NegativeNumberException):
    return JSONResponse(
        status_code=420,
        content= "message" : f" Hi, why do you need cats to be negative {exception.cats_to_return}"
    )


@app.get("/")
async def read_all_cats(cats_to_return: Optional[int] = None):
    if cats_to_return < 0:
        raise NegativeNumberException(cats_to_return= cats_to_return)
    if len(CATS) < 1:
        create_cat_no_api()
    if cats_to_return and len(CATS) >= cats_to_return > 0:
        i = 1
        new_cats = []
        while i <= cats_to_return:
            new_cats.append(CATS[i - 1])   
            i += 1
        return new_cats
    return CATS


@app.get("/cat/{cat_id}")
async def read_cat(cat_id: UUID):
    for x in CATS:
        if x.id == cat_id:
            return x
        raise raise_cat_cannot_be_found_exception

@app.get("/cat/rating/{cat_id}", response_model= CatsWithoutRatings)
async def read_cat_no_ratings(cat_id: UUID):
    for x in CATS:
        if x.id == cat_id:
            return x
        raise raise_cat_cannot_be_found_exception

@app.post("/")
async def create_cat(cat: Cat):
    CATS.append(cat)
    return cat

@app.get("/cat_id")
async def update_cat(cat_id: UUID, cat: Cat):
    counter = 0
    for x in CATS:
        counter += 1
        if x.id == cat_id:
            CATS[counter - 1] = cat
            return CATS[counter - 1]


@app.delete("/{cat_id}")
async def delete_cat(cat_id: UUID):
    counter = 0

    for x in CATS:
        counter += 1
        if x.id == cat_id:
            del CATS[counter - 1]
            return f'ID:{cat_id} deleted'
    raise  raise_cat_cannot_be_found_exception()

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
    

def raise_cat_cannot_be_found_exception():
    raise HTTPException (status_code= 404,
                         detail= "Cat no where to be found",
                         headers= {
                            "X-Header_Error":
                            "Nothing to be found with that UUID"
                         })