from pydantic import BaseModel

class Alien(BaseModel):
    name: str
    alien_type: str
    home_planet: str
    power: list[str]