# conftest.py
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from todo.models import Todo
from rest_framework import status

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    """Creates a standard test user."""
    user = User.objects.create_user(username="testuser", password="testpassword")
    return user

@pytest.fixture
def another_user(db):
    """Creates another user for testing unauthorized access."""
    user = User.objects.create_user(username="anotheruser", password="testpassword")
    return user

@pytest.fixture
def auth_client(api_client, test_user):
    """Returns an authenticated client for the test_user."""
    response = api_client.post("/api/token/", {"username": "testuser", "password": "testpassword"})
    assert response.status_code == status.HTTP_200_OK
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

@pytest.fixture
def sample_todo(test_user):
    """Creates a sample Todo for the test_user."""
    return Todo.objects.create(user=test_user, title="Sample Task", description="A sample task", completed=False)
