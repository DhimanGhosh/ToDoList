from django.forms import ModelForm
from .models import Profile

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
