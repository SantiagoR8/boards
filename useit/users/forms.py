from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    identification = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'identification'}))
    avatar = forms.ImageField(required=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 
        			'identification', 'avatar')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 
        			'identification', 'avatar')