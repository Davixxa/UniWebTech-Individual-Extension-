from django import forms
from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'text')
        widgets = {
            'rating': forms.NumberInput(attrs={
                "class": "form-control"
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'game': forms.Select(attrs={
                'class': 'form-control'
            }),
        }