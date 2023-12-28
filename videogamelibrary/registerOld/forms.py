from django import forms 
from .models import regularUser
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control'
            }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control'
            }))
    
    # Attrs is present for applying boostrap styling
    

    class Meta:
        model = regularUser
        fields = ('username', 'email', 'password')
        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control'
            }),

        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control'
            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control'
            }))