import requests

BASE_URL = "http://127.0.0.1:8000"

def show_all_aliens():
    response = requests.get(f"{BASE_URL}/aliens")
    aliens = response.json()
    for alien in aliens:
        print(alien["name"])