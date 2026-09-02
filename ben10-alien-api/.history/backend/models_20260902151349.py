from pydantic import BaseModel

if __name__ == "__main__":
    test = Alien(
        name="Heatblast",
        alien_type="Pyronite",
        home_planet="Pyros",
        powers=["fire manipulation", "flight"]
    )
    
    print(test)
    print(test.model_dump())