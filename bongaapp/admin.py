from django.contrib import admin

from bongaapp.models import Image, Profile, Comment, Like

# Register your models here.

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)