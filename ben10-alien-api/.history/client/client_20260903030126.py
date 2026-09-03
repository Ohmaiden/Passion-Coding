import requests

BASE_URL = "http://127.0.0.1:8000"

def show_all_aliens():
    response = requests.get(f"{BASE_URL}/aliens")
    aliens = response.json()
    for alien in aliens:
        print(alien["name"])
        
def show_random_alien():
    response = requests.get(f"{BASE_URL}/aliens/random")
    alien = response.json()
    print(alien["name"])
    print(alien["alien_type"])
    print(alien["home_planet"])
    print(alien["powers"])
               
        
show_all_aliens()
show_random_alien()