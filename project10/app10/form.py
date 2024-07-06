from django import forms
from . models import login
class loginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    class Meta:
        model=login
        fields=('Email','Password')

class registerform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    class Meta:
        model=login
        fields='__all__'

class updateform(forms.ModelForm):
    class Meta:
        model=login
        fields=('Name','Age','Place','Email')

class changepasswordform(forms.ModelForm):
    oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    newpassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)



