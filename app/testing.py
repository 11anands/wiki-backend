import json
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from app.main import app


# Initialize the application for testing
@pytest.fixture()
def client():
    return TestClient(app=app)


# Testing the GET /search endpoint
def test_search():
    client = TestClient(app)
    response = client.get("/search")
    assert response.status_code == status.HTTP_200_OK


# Testing the POST /search endpoint
def test_post_search():
    client = TestClient(app)
    data = {"search_value": "Folic Acid"}
    response = client.post("/search", data=data)
    assert response.status_code == status.HTTP_200_OK


# Testing the GET /drugs endpoint
def test_drugs():
    client = TestClient(app)
    response = client.get("/drugs")
    assert response.status_code == status.HTTP_200_OK
