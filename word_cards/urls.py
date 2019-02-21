from django.urls import path
from . import views
app_name = 'base_app'

urlpatterns = [
    path('add_new_words/', views.add_new_words, name='add_new_words'),
    path('add_new_words/base_app/word_added_successfully/', views.word_added_successfully),
    path('training/', views.training, name='training'),
    path('main_training_page/', views.main_training_page, name='main_training_page'),
    path('table_of_words/', views.table_of_words, name='table_of_words'),
    path('flash_cards', views.flash_cards, name='flash_cards'),
]





