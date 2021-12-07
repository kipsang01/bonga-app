from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

    
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'bonga/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=50,blank=True)
    author = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)

    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_caption(self,newcaption):
        self.caption = newcaption
        self.save()
        
    @classmethod    
    def all_images(self):
        images= Image.objects.all()
        return images
    
    @classmethod    
    def search_user(self, username):
        user= User.objects.filter(username=username).first()
        return user
    
    
class Comment(models.Model):
    image = models.ForeignKey(Image,related_name='comments',on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.content
    
    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()
    

class Like(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,related_name='likes',on_delete=models.CASCADE)
    
    
    def __str__(self):
          return '{} by {}'.format(self.image, self.author)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'image'], name="unique_like"),
        ]
    def save_like(self):
        self.save()
        
    def delete_like(self):
        self.delete()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    profile_pic = models.ImageField(upload_to = 'bonga/') 
    
    def __str__(self):
        return str(self.user)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    