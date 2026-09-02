from fastapi import FastAPI
import json
from models import Alien
import random

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