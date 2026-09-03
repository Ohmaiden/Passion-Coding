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
               
def show_alien_by_name(name):
    response = requests.get(f"{BASE_URL}/aliens/{name}")
    if response.status_code == 404:
        print(f"Alien '{name}' not found")
    else:
        alien = response.json()
        print(alien["name"])
        print(alien["alien_type"])
        print(alien["home_planet"])
        print(alien["powers"])

        
def main_menu():
    while True:
        print("\n--- Ben 10 Alien Finder ---")
        print("1. Show all aliens")
        print("2. Show random alien")
        print("3. Search alien by name")
        print("4. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_all_aliens()
        elif choice == "2":
            show_random_alien()
        elif choice == "3":
            show_alien_by_name()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")