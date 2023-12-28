from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Class Constructor - This is apparently a way to set styling on default fields.
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__()

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
