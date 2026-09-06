from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_aliens():
    response = client.get("/aliens")
    assert response.status_code == 200
    
def test_get_random_alien():
    response = client.get("/aliens/random")
    assert response.status_code == 200
    
def test_get_alien_by_name():
    response = client.get("/aliens/Heatblast")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Heatblast"
    
def test_get_alien_by_name_not_found():
    response = client.get("/aliens/FakeAlien123")
    assert response.status_code == 404