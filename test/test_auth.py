import pytest
import sys
import os
from fastapi.testclient import TestClient   # 引入测试客户端

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app
from app.schemas.user_schema import UserRegistrationSchema

@pytest.fixture
def client():
    return TestClient(app)


def test_register_success(client):
    user_data: UserRegistrationSchema = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }

    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 200
    assert response.json()["message"] == "ok"
    assert response.json()["username"] == user_data["username"]


