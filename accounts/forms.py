from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        # combine fields of User and UserCreationForm
        fields = ['username', 'email', 'password1', 'password2']
