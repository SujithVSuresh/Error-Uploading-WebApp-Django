import django
from django.db import models
from django.http import request
from .models import ErrorListing
from django import forms
from django.forms import ModelForm, fields

class ErrorListingForm(forms.ModelForm):
    error_body = forms.CharField(label='Enter error:', widget=forms.Textarea(attrs={'rows':'2', 'placeholder':'Enter the error..'}))
    error_description = forms.CharField(label='Error description:', widget=forms.Textarea(attrs={'rows':'3', 'placeholder':'Describe the error...'}))
    error_reason = forms.CharField(label='Error reason:', widget=forms.Textarea(attrs={'rows':'3', 'placeholder':'What causes this error...'}))
    error_solution = forms.CharField(label='Error solution:', widget=forms.Textarea(attrs={'rows':'3', 'placeholder':'What is the solution of this error...'}))

    class Meta:
        model = ErrorListing
        fields = ['error_body', 'error_description', 'error_reason', 'error_solution', 'mode', 'author']
        widgets = {'author': forms.HiddenInput()}

