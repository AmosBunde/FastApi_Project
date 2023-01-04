from fastapi import FastAPI

app = FastAPI()


CATS = {
    'cat_01': {'breed': 'Abyssinian', 'size': 'Large', 'energy': 'High', 'shedding': 'Minimal'},
    'cat_02': {'breed': 'Bengal', 'size': 'Small', 'energy': 'Low', 'shedding': 'Heavy'},
    'cat_03': {'breed': 'Bombay', 'size': 'Medium', 'energy': 'High', 'shedding': 'Minimal'},
    'cat_04': {'breed': 'Birman', 'size': 'Large', 'energy': 'High', 'shedding': 'Minimal'},
    'cat_05': {'breed': 'Burmese', 'size': 'Huge', 'energy': 'Low', 'shedding': 'Heavy'},

}

@app.get("/")
async def get_cat_breeds():
    return CATS

@app.get("/cats/mycats")
async def get_my_favourite_cat():
    return {"breed": "Bengal"}

@app.get("/cats/{breed}")
async def pick_cats(breed: str):
    return {"breed": breed}    