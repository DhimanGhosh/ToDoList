from todo.serializers import TodoSerializer
from todo.models import Todo
import pytest

@pytest.mark.django_db
def test_todo_serializer():
    todo = Todo.objects.create(title="Test Task", description="Test description", completed=False)
    serializer = TodoSerializer(todo)
    data = serializer.data
    assert data["title"] == "Test Task"
    assert data["completed"] is False
