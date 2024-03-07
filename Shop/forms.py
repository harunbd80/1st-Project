from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User

class CustomerRegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': "Enter your Email"}
        # labels = {'username': forms.Textarea(attrs={'class': 'form-control'})}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}
#Login
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control'}))