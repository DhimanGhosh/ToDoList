from django.forms import ModelForm
from .models import Todo
from django import forms
import re


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ['completed', 'user']
        field_order = ["title", "description"]
        labels = {
            "title": "Task Title",
            "description": "Task Description",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Add the title of the task"}),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Add the description of the task",
                "rows": "5",
                "style": "resize: none;"
            }),
        }
        error_messages = {
            "title": {
                "required": "Task title is required!",
                "max_length": "Title cannot exceed 50 characters!",
                "invalid": "Invalid characters in title!",
            },
            "description": {
                "max_length": "Description cannot exceed 500 characters!",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["description"].required = False

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 50:
            raise forms.ValidationError("Task title length should be within 50 characters!")
        if re.findall(r'[^a-zA-Z0-9 ]', title):
            raise forms.ValidationError("Task title should have only alphanumeric characters!")
        return title

    def clean_description(self):
        description = self.cleaned_data["description"]
        if not description:
            return ""  # Return empty string without raising errors
        if len(description) > 500:
            raise forms.ValidationError("Task description length should be within 500 characters!")
        return description

    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            print(f"Form is invalid: Errors: {self.errors}")
        return valid
