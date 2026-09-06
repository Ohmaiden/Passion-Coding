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
    
def test_filter_by_series():
    response = client.get("/aliens", params={"series": "Classic"})
    assert response.status_code == 200
    data = response.json()
    assert all(alien["series"] == "Classic" for alien in data)
    
def test_pagination_limit():
    response = client.get("/aliens", params={"limit": 5})
    assert response.status_code == 200
    data = response.json()
    names = [alien["name"] for alien in data]
    assert names == sorted(names)
    
def test_sort_by_name():
    response = client.get("/aliens", params={"sort_by": "name", "limit": 5})
    assert response.status_code == 200
    data = response.json()
    names = [alien["name"] for alien in data]
    assert names == sorted(names)
    
def test_search_powers():
    response = client.get("/aliens", params={"search": "fire"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    