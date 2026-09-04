from pydantic import BaseModel

class UltimateForm(BaseModel):
    name: str
    powers: list[str]
class Alien(BaseModel):
    name: str
    alien_type: str
    home_planet: str
    powers: list[str]
    series: str
    also_known_as: list[str] | None = None
    ultimate_form: UltimateForm | None = None
    
if __name__ == "__main__":
    test = Alien(
        name="Heatblast",
        alien_type="Pyronite",
        home_planet="Pyros",
        powers=["fire manipulation", "flight"],
        series="Classic"
    )
    
    print(test)
    print(test.model_dump())