from pydantic import BaseModel

class Alien(BaseModel):
    name: str
    alien_type: str