from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('content/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret_class/', views.SecretPage.as_view(), name='secret_class'),
    path('accounts/', include('django.contrib.auth.urls')), # login/ logout/ password_change
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate, name='activate'),
]
