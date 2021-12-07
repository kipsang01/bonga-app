from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
from bongaapp.models import Image, Profile ,Comment, Like
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
    if user == request.user:
        return redirect('my_profile',username = user.username)
    profile = get_object_or_404(Profile,id = user.id)
    posts = Image.objects.filter(author=user)
    return render(request, 'userprofile.html', {'user': user,'profile':profile,'posts':posts})

#logged in user profile
@login_required(login_url='/accounts/login')
def my_profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    posts = Image.objects.filter(author=user)
    return render(request, 'profile.html', {'user': user,'posts':posts})

# Edit profile
@login_required(login_url='/accounts/login')
def edit_profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    profile = get_object_or_404(Profile,user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profileform = form.save(commit=False)
            profileform.user = user
            profileform.save()
            messages.success(request,('Update saved'))
        return redirect('my_profile',username =user.username)
           
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
        return HttpResponseRedirect(request.path_info)
           
    else:
        form = ImageForm()
        
    return render(request,'add_post.html', {'form':form})
    
# Liking post
@login_required(login_url='/accounts/login')
def like_image(request, image_id):
    image = get_object_or_404(Image,id = image_id)
    like = Like.objects.filter(image = image ,author = request.user).first()
    if like is None:
        like = Like()
        like.image = image
        like.author = request.user
        like.save()
    else:
        like.delete()
    return redirect('home')




# one post page
def post(request,image_id):
    image =  get_object_or_404(Image,id = image_id)
    comments = Comment.objects.filter(image=image).all()
    current_user = request.user
    
    if request.method =='POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            
            comment.image = image
            comment.save()
        return redirect('post',image_id=image.id)
    else:
        
        form = CommentForm()
    return render(request, 'post.html', {'image': image, 'form':form, 'comments':comments})

# search users by usernames
def search_user(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        print(search_term)
        found_user = Image.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{'founduser':found_user})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



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