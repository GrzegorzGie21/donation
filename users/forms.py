from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email']


class ChangeUserForm(UserChangeForm):
    username = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = '__all__'