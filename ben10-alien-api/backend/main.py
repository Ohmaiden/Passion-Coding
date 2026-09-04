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
def get_all_aliens(series: str | None = None, skip: int = 0, limit: int = 10):
    result = aliens
    if series:
        matches = []
        for alien in result:
            if alien.series.lower() == series.lower():
                matches.append(alien)
        result = matches
    return result[skip: skip + limit]

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