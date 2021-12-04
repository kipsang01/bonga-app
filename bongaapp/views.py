from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from bongaapp.models import Image
from .forms import  RegisterUserForm
from .email import send_welcome_email

# Create your views here.
def home(request):
    title= ' Home is working'
    return render(request, 'home.html', {'title':title})


# Register user
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # Send email upon registration
            # recipient = EmailRecipients(name = username,email =email)
            # recipient.save()
            send_welcome_email(username,email)
            
            #authenticate and login user
            user = authenticate(username = username,password=password)
            login(request,user)
            messages.success(request,('Registration successfull and logged in'))
            return redirect('home')
           
            #HttpResponseRedirect('news_today')
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})


# def login_user(request):
#     if request.method == 'POST':
        
    
    
    
def logout_user(request):
    logout(request)
    title= ' Home is working'
    return redirect('home')