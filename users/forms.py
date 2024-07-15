from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'department', 'password1', 'password2']

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'department', 'profile_image']