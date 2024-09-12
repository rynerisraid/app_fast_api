import pytest
from fastapi.testclient import TestClient
from ...main import app
from ...app.schemas.user_schema import UserRegistrationSchema
from ...app.services.auth.services import get_user_by_email, get_user_by_name, create_user, hash_password

@pytest.fixture
def client():
    return TestClient(app)

def test_register_success(client):
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 200
    assert response.json()["message"] == "ok"
    assert response.json()["username"] == user_data["username"]

def test_register_email_exists(client):
    user_data = {
        "username": "testuser",
        "email": "existing@example.com",
        "password": "testpassword"
    }
    # 先创建一个用户以确保邮箱已存在
    existing_user = UserRegistrationSchema(**user_data)
    hashed_password = hash_password(existing_user.password)
    create_user(user=existing_user, hashed_password=hashed_password)
    
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "邮箱已存在"
