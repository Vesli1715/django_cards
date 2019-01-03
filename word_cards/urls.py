from django.urls import path, re_path

from . import views


app_name = 'word_cards'
urlpatterns = [
   
	path('', views.base),
	path('add_words/', views.add_words, name='add_words'),
    path('training_flip_cards', views.training_flip_cards, name='flip_cards'),
    path('choice/', views.choose_right_answer, name='choice'),
	path('words_list/last_ten/', views.delete_word),
    
    path('words_list/last_ten/', views.show_last_ten, name='last_ten'),
    path('words_list/last_twenty/', views.show_last_twenty, name='last_twenty'),
    path('words_list/last_fifty/', views.show_last_fifty, name='last_fifty'),
    path('words_list/all/', views.show_all_words_list, name='all_words_list'),
    

    path('add_words/word_cards/just_been_added', views.just_been_added),
    


   
    
]