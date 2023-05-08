from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea)


