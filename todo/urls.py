from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    
    # Main ToDo App
    path("todos/", views.todos, name="todos"),
    path("add/", views.add, name="add"),
    path("update/<int:todo_id>", views.update, name="update"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("toggle_completed/<int:todo_id>/", views.toggle_completed, name="toggle_completed"),
]
