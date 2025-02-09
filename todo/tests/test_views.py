import pytest
from rest_framework import status

@pytest.mark.parametrize(
    "title, description, expected_status",
    [
        ("Valid Task", "This is a valid task", status.HTTP_201_CREATED),
        ("", "Missing title", status.HTTP_400_BAD_REQUEST),  # Missing title
        ("A" * 300, "Title too long", status.HTTP_400_BAD_REQUEST),  # Title exceeds max length
    ]
)
def test_create_todo(auth_client, title, description, expected_status):
    """Test creating todos with various input cases."""
    data = {"title": title, "description": description}
    response = auth_client.post("/api/todos/", data)
    assert response.status_code == expected_status

def test_get_todo_list(auth_client, sample_todo):
    response = auth_client.get("/api/todos/")
    assert response.status_code == 200
    assert len(response.data) == 1

def test_get_todo_list_unauthorized(api_client):
    """Test that unauthenticated users receive 401 Unauthorized."""
    response = api_client.get("/api/todos/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_delete_todo_unauthorized(auth_client, another_user):
    """Test that a user cannot delete another user's todo."""
    from todo.models import Todo
    todo = Todo.objects.create(user=another_user, title="Unauthorized Task")
    
    response = auth_client.delete(f"/api/todos/{todo.id}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND  # Not found because it's not their todo
