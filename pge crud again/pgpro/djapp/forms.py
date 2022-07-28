from dataclasses import fields
from pyexpat import model
from unicodedata import name
from django import forms
from django import forms 
from .models import user
class studentreg(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']

    widgets={
        'name' :forms.TextInput(attrs={'class':'form-control'}),
        'email' :forms.EmailInput(attrs={'class':'form-control'}),
        'password' :forms.PasswordInput(attrs={'class':'form-control'})
    }

