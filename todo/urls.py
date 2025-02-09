from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("", views.home, name="home"),
    
    # Main ToDo App
    path("todos/", views.todos, name="todos"),
    path("add/", views.add, name="add"),
    path("update/<int:todo_id>", views.update, name="update"),
    path('update_task_status/<int:todo_id>/', views.update_task_status, name='update_task_status'),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("toggle_completed/<int:todo_id>/", views.toggle_completed, name="toggle_completed"),
    
    # REST APIs
    path("api/todos/", views.TodoListCreateAPIView.as_view(), name="todo-list-create"),
    path("api/todos/<int:pk>/", views.TodoRetrieveUpdateDestroyAPIView.as_view(), name="todo-detail"),
    
    # Tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
