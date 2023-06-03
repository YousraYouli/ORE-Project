from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput



class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class ContactForm(forms.Form):
    name = forms.CharField(max_length=255,label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your massage',widget=forms.Textarea)
    phone=forms.IntegerField(label='Your phone number')






       