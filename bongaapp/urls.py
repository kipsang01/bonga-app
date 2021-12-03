from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register_user, name='registration'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

