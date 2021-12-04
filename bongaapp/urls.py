from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-image/', views.post_image, name='add_post'),
    path('accounts/register/', views.register_user, name='registration'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
