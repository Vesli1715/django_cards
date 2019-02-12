
from django.urls import path, include
from . import views


urlpatterns = [
    path('content/', views.index, name='index'),
    path('singup/', views.singup, name='singup'),
    path('accounts', include('django.contrib.auth.urls')),
]