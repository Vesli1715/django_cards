from django.urls import path
from . import views
app_name = 'base_app'

urlpatterns = [
    path('add_new_words/', views.add_new_words, name='add_new_words'),
    path('word_added_successfully/', views.word_added_successfully, name='word_added_successfully'),
    path('table_of_words/', views.table_of_words, name='table_of_words'),
    path('flash_cards/', views.flash_cards, name='flash_cards'),
    path('main_training_page/', views.main_training_page, name='main_training_page'),
    path('training_en/', views.training_english_word, name='training_english_word'),
    path('training_ua/', views.training_ukrainian_word, name='training_ukrainian_word'),
]





