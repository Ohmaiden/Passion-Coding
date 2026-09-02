from fastapi import FastAPI
import json
from models import Alien

app = FastAPI()

with open("data/aliens.json", "r") as file:
    aliens_data = json.load(file)