import json
from .forms import TodoForm, ProfileUpdateForm
from .models import Todo
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def home(request):
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
            return redirect("view")
    else:
        form = TodoForm()
    return render(request, "todo/add.html", {"form": form})

@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)  # Ensure user owns the ToDo
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("view")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todo/update.html", {"form": form})

@login_required
def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)  # Ensure user owns the ToDo
    todo.delete()
    return redirect("view")

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def deactivate_account(request):
    if request.method == "POST":
        entered_username = request.POST.get("username", "").strip()

        if entered_username != request.user.username:
            messages.error(request, "Incorrect username. Account deletion canceled.")
            return redirect("profile")  # Redirect back to profile

        user = request.user
        logout(request)  # Log user out before deletion
        user.delete()  # Delete user from auth_user table
        messages.success(request, "Your account has been successfully deleted.")
        return redirect("register")  # Redirect to register page after deletion

@login_required
def update_profile_picture(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm()

    return render(request, "users/update_profile_picture.html", {"form": form})
