from django.shortcuts import render
from .forms import  RegisterUserForm

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
            password = form.cleaned_data['password']
            
           # recipient = NewsLetterRecipients(name = name,email =email)
            
            #recipient.save()
            
            #send_welcome_email(name,email)
            #HttpResponseRedirect('news_today')
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})