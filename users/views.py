from .forms import ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('password_change_done')

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
