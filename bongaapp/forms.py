from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Image,Comment


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    
    class  Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
class ImageForm(ModelForm):
    
    
    class Meta:
        model = Image
        fields = ('image','name','caption','location' )