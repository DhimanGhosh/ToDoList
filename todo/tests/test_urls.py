from django.urls import reverse, resolve
from todo.views import TodoListCreateAPIView

def test_todo_list_url():
    url = reverse("todo-list-create")
    assert resolve(url).func.view_class == TodoListCreateAPIView
