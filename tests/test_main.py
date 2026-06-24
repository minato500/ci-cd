from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "Application is running cleanly."}

def test_read_secure_data():
    response = client.get("/api/v1/data")
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"] == "Secure pipeline deployment complete."
