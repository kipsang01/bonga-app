from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
from bongaapp.models import Image, Profile ,Comment
from django.contrib.auth.models import User
from .forms import  RegisterUserForm,ImageForm,ProfileForm,CommentForm
from .email import send_welcome_email

# Create your views here.
def home(request):
    title= ' Home'
    form = CommentForm()
    images = Image.all_images()
    current_user = request.user
    
    if request.method =='POST':
        if 'postComment' in request.POST:
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.author = current_user
            comment.save()
            
    
    return render(request, 'home.html', {'title':title, 'images':images, 'form':form})

# Page for profile
def user_profile(request,username):
    user = User.objects.filter(username=username).first()
    profile = get_object_or_404(Profile,id = user.id)
    posts = Image.objects.filter(author=user)
    return render(request, 'profile.html', {'user': user,'profile':profile,'posts':posts})

# Edit profile
@login_required(login_url='/accounts/login')
def edit_profile(request,username):
    user = User.objects.filter(username=username).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,('Update saved'))
        return redirect('user_profile')
           
    else:
        form = ProfileForm()
    
    return render(request, 'edit_profile.html', {'form':form, 'user': user})



 # Image posting page
@login_required(login_url='/accounts/login')
def post_image(request):
    if request.method == 'POST':
        current_user = request.user
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
            messages.success(request,('Image Posted!'))
        return redirect('home')
           
    else:
        form = ImageForm()
        
    return render(request,'add_post.html', {'form':form})
    

# one post page
def post(request,image_id):
    image =  get_object_or_404(Image,id = image_id)
    comments = Comment.objects.filter(image=image).all()
    form = CommentForm()
    current_user = request.user
    
    if request.method =='POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = current_user
        comment.image = image
        comment.save()
        return redirect('post')
        
    return render(request, 'post.html', {'image': image, 'form':form, 'comments':comments})





# Register user
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            
            #authenticate and login user
            user = authenticate(username = username,password=password)
            login(request,user)
            messages.success(request,('Registration successfull and logged in'))
            return redirect('home')
           
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})

    # Logout    
def logout_user(request):
    logout(request)
    title= ' Home is working'
    return redirect('home')