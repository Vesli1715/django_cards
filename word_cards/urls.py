from django.urls import path
from . import views
app_name = 'word_cards'

urlpatterns = [

    path('', views.base),
    path('add_words/', views.add_words, name='add_words'),
    path('delete/', views.de, name='delete_word'),
    path('add_words/word_cards/just_been_added', views.just_been_added),
    path('training_flip_cards', views.training_flip_cards, name='flip_cards'),
    path('polls/', views.training ),


    path('add_new_words/', views.add_new_words, name='add_new_words'),
    path('add_new_words/base_app/word_added_successfully/', views.word_added_successfully ),
    path('training/', views.training, name='training'),
    path('main_training_page/', views.main_training_page, name='main_training_page'),
    path('table_of_words/', views.table_of_words, name='table_of_words')
]





