from django.urls import path, include
from . import views


urlpatterns = [
    path('content/', views.index, name='index'),
    path('singup/', views.singup, name='singup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret_class/', views.SecretPage.as_view(), name='secret_class'),
    path('accounts/', include('django.contrib.auth.urls')),
]