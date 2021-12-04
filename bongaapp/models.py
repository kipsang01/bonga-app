from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

    
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'bonga/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=50,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)

    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    @classmethod    
    def all_images(self):
        images= Image.objects.all()
        return images
    
    
class Comment(models.Model):
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.content
    
    

class Like(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.author


class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    profile_pic = models.ImageField(upload_to = 'bonga/') 
    
    def __str__(self):
        return str(self.user)
    