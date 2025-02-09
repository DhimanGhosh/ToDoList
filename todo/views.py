import json
from .forms import TodoForm
from .models import Todo
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("todos")
    return redirect("login")

@login_required
def todos(request):
    todos = Todo.objects.filter(user=request.user)  # Show only logged-in user's ToDos
    return render(request, "todo/index.html", {'todos': todos})

@login_required
def add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Assign ToDo to the logged-in user
            todo.save()
            return redirect("todos")
    else:
        form = TodoForm()
    return render(request, "todo/add.html", {"form": form})

@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)  # Ensure user owns the ToDo
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, "Task updated successfully!")
            else:
                messages.info(request, "No changes made!")
            return redirect("todos")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todo/update.html", {"form": form})

@login_required
def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)  # Ensure user owns the ToDo
    todo.delete()
    return redirect("todos")

def toggle_completed(request, todo_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON request
            completed_status = data.get("completed", False)  # Get the completed value

            todo = get_object_or_404(Todo, id=todo_id)
            todo.completed = completed_status  # Update field
            todo.save()  # Save to database

            return JsonResponse({"status": "success", "completed": todo.completed})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error"}, status=400)

def custom_404(request, exception):
    return render(request, "404.html", status=404)


## REST APIs

# List and Create Todos
class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete a single Todd
class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
