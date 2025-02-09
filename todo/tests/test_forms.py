from todo.forms import TodoForm
import pytest

@pytest.mark.django_db
def test_todo_form_valid():
    form = TodoForm(data={"title": "Test Task", "description": "Test description"})
    assert form.is_valid() is True

@pytest.mark.django_db
def test_todo_form_invalid():
    form = TodoForm(data={"title": ""})  # Missing title
    assert form.is_valid() is False
    assert "title" in form.errors
