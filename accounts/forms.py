from django import forms
from django.contrib.auth import get_user_model
from accounts.models import userDetails

User = get_user_model()


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateUserProfileform(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ["phone", "house_no", "street", "city", "state", "zipcode", "img"]
