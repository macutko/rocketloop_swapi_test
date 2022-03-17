from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_auth_user():
    response = client.post("/login", json={"username": "admin", "password": "notadmin123"})
    assert response.status_code == 200
    assert response.json() == {"message": "Success!"}


def test_films():
    response = client.get("/api/v1/films")


def test_people():
    response = client.get("/api/v1/people")
