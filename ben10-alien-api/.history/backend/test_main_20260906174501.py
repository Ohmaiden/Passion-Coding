from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_aliens():
    response = client.get("/aliens")
    assert response.status_code == 200
    