from django.urls import path, include

from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # default django auth urls
    path('signup/', views.signup, name='signup'),
]
