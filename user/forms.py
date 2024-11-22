from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
  

   

    email = forms.CharField(
        widget=forms.TextInput(attrs={
              'class': 'w-full px-4 py-2 mt-1 border rounded-lg focus:ring-blue-500 focus:border-blue-500 border-gray-300',
            'placeholder': 'Enter your email',    
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 mt-1 border rounded-lg focus:ring-blue-500 focus:border-blue-500 border-gray-300',
            'placeholder': 'Enter your password',
        })
    )
  
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 mt-1 border rounded-lg focus:ring-blue-500 focus:border-blue-500 border-gray-300',
            'placeholder': 'Enter your password',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 border rounded-lg focus:ring-blue-500 focus:border-blue-500 border-gray-300',
                'placeholder': 'Enter your username',
            }),
           
        }
       


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 mt-1 border rounded-lg focus:ring-blue-500 focus:border-blue-500 border-gray-300',
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 mt-1 border rounded-lg focus:ring-blue-500 focus:border-blue-500 border-gray-300',
            'placeholder': 'Enter your password',
        })
    )