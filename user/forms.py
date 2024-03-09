from cProfile import Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from user.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
    # password = forms.PasswordInput()
    first_name = forms.CharField(label='First Name',)
    last_name = forms.CharField(label='Last Name', )

    class Meta:
        model = User
        fields: tuple = 'username', 'email', 'first_name', 'last_name', 'password1', 'password2'


CITY: list = [
    ('Izmir', 'Izmir'),
    ('Ankara', 'Ankara'),
    ('Istanbul', 'Istanbul')
]


class UserUpdateForm(UserChangeForm):
    class Meta:
        model: User = User
        fields: tuple = 'username', 'email', 'first_name', 'last_name'
        widgets: dict = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields: tuple = 'phone_number', 'address', 'city', 'country', 'profile_pic'
        widgets: dict = {
            'phone_number': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'input', 'placeholder': 'adress'}),
            'city': forms.Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': forms.TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': forms.FileInput(attrs={'class': 'input', 'placeholder': 'image'})
        }

