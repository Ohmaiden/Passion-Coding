from fastapi import FastAPI, HTTPException
import json, random
from models import Alien


app = FastAPI()

with open("data/aliens.json", "r") as file:
    aliens_data = json.load(file)
    
aliens = []
for alien in aliens_data:
    aliens.append(Alien(**alien))
    
@app.get("/aliens")
def get_all_aliens():
    return aliens

@app.get("/aliens/random")
def get_random_alien():
    return random.choice(aliens)

@app.get("/aliens/{name}")
def get_alien_by_name(name: str):
    for alien in aliens:
        if alien.name.lower() == name.lower():
            return alien
        if alien.also_known_as:
            for alt_name in alien.also_known_as:
                if alt_name.lower() == name.lower():
                    return alien
    raise HTTPException(status_code=404, detail="Alien not found")