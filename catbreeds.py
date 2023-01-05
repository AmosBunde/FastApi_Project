from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


CATS = {
    'cat_01': {'breed': 'Abyssinian', 'size': 'Large', 'energy': 'High', 'shedding': 'Minimal'},
    'cat_02': {'breed': 'Bengal', 'size': 'Small', 'energy': 'Low', 'shedding': 'Heavy'},
    'cat_03': {'breed': 'Bombay', 'size': 'Medium', 'energy': 'High', 'shedding': 'Minimal'},
    'cat_04': {'breed': 'Birman', 'size': 'Large', 'energy': 'High', 'shedding': 'Minimal'},
    'cat_05': {'breed': 'Burmese', 'size': 'Huge', 'energy': 'Low', 'shedding': 'Heavy'},

}



@app.get("/")
async def get_cat_breeds(skip_cat: Optional[str] =None):
    if skip_cat:
        new_cats = CATS.copy()
        del new_cats[skip_cat]
        return new_cats
    return CATS
   

@app.get("/cats/mycats")
async def get_my_favourite_cat():
    return {"breed": "Bengal"}

@app.get("/cats/{breed}")
async def pick_cats(breed: str):
    return {"breed": breed}    


@app.post("/")
async def create_cat(cat_breed, cat_size):
    current_cat_id = 0

    if len(CATS)> 0:
        for cat in CATS:
            x = int(cat.split('_')[])
            if x > current_cat_id:
                current_cat_id = x

    CATS[f'cat_{current_cat_id + 1}'] = {'breed': cat_breed, 'size': cat_size}
    return CATS[f'cat_{current_cat_id + 1}']
