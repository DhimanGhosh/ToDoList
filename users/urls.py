from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Users
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("deactivate/", views.deactivate_account, name="deactivate_account"),
    path("update-profile-picture/", views.update_profile_picture, name="update_profile_picture"),
] + \
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
