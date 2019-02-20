from random import shuffle
from django.http import HttpResponseRedirect , HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WordsForm, DeleteForm, SimpleForm
from .models import Words


def base(request):
    return render(request, 'word_cards/content.html')


def add_words(request):
    if request.method == 'POST':
        en = request.POST['en_word'].lower()
        ua = request.POST['ua_word'].lower()
        if en.isalpha() and ua.isalpha():
            field = WordsForm(request.POST)
            field.save()
            data = {'en': en, 'ua': ua}
            return redirect('word_cards/just_been_added', {'data': data}) # always must be redirect
    else:
        form = WordsForm()
    return render(request, 'word_cards/add_words.html', {'form': form})


def just_been_added(request):
    word = Words.objects.all().order_by('-id')[:1]
    return render(request, 'word_cards/just_been_added.html', {'word': word})


def de(request):
    last_record = Words.objects.all().order_by('-id')[:1]
    for i in last_record:
        i.delete()
    return render(request, '/sfds/')


def delete_word(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            word = request.POST.get('delete_word', 'error')
            if word:
                print(word)
                Words.objects.filter(en_word=word).delete()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeleteForm()
    fields = Words.objects.all().order_by('-id')[:10]
    D = {'form': form, 'fields': fields}
    return render(request, 'word_cards/all_words_list.html', D)

def show_record_data(request):
    en = request.POST['english_word']
    ua = request.POST['ukrainian_word']
    data = {'en': en, 'ua': ua}
    return render(request, 'word_cards/all_words_list.html', data)


def training_flip_cards(request):
    fields = Words.objects.all().order_by('-id')[:10]
    return render(request,'word_cards/training_flip_cards.html',{'fields': fields})


def choose_right_answer(request):
    query = list(Words.objects.all().order_by('-id')[:5])
    L=[]
    for items in query:
        s = str(items)
        words = s.split(' ')
        L.append(words) 

    all_words = {key: value for (value, key) in L}  
    en_words = []
    ua_words = []   
    for en, ua in all_words.items():
        en_words.append(en)
        ua_words.append(ua)

    data = {
        'en_words':en_words,
        'ua_words':ua_words,
        'all_words':all_words
    }
    return render(request, 'word_cards/choice.html',data)



def some():
    pass

@login_required
def add_new_words(request):
    if request.method == 'POST':
        en = request.POST['en_word'].lower()
        ua = request.POST['ua_word'].lower()
        if en.isalpha() and ua.isalpha():
            field = WordsForm(request.POST)
            field.save()
            data = {'en': en, 'ua': ua}
            return redirect('base_app/word_added_successfully', {'data': data})  # always must be redirect
    else:
        form = WordsForm()
    return render(request, 'base_app/add_new_words.html', {'form': form})


def word_added_successfully(request):
    return render(request, 'base_app/word_added_successfully.html')




def table_of_words(request):
    fields = Words.objects.all().order_by('-id')

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            word = request.POST.get('delete_word', 'error')
            if word:
                print(word)
                Words.objects.filter(en_word=word).delete()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            D = {'form': form, 'fields': fields}
            return render(request, 'base_app/table_of_words.html',D)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = DeleteForm()
    fields = Words.objects.all().order_by('-id')[:10]
    D = {'form': form, 'fields': fields}

    return render(request, 'base_app/table_of_words.html', D)





""" ---------- TRAINING BLOCK ------------- """

def main_training_page(request):
    return render(request, 'base_app/main_training_page.html')


def list_last5_from_table():
    """returns list of last 5 records in db in format [['en_w','ua_word'],[...]]
    this function for using in training func"""
    query = list(Words.objects.all().order_by('-id')[:5])
    L = []
    for items in query:
        s = str(items)
        words = s.split(' ')
        L.append(words)
    return L

w_index = 0
@login_required
def training(request):
    """The function is designed to run the training_last_five.html page.
    Using dictionaries (keys -> value) logic is the right choice"""

    all_words = {key: value for (key, value) in list_last5_from_table()}
    list_of_en_words = [en for en, ua in all_words.items()]
    list_of_ua_words = [ua for en, ua in all_words.items()]
    shuffle(list_of_ua_words)

    user_choice = ''
    if request.method == 'POST':
        d = dict(request.POST)
        for k, v in d.items():
            user_choice = v[0]   # return word selected by user from radio button form

    global w_index
    question_word = list_of_en_words[w_index]
    result = ''
    next = False
    if request.method == 'POST':
        if all_words[question_word] == user_choice:
            result = list_of_en_words[w_index] + " --> " + user_choice
            next = True
        else:
            result = "Wrong"

    if w_index >= 4:
        return render(request, 'base_app/main_training_page.html')
    elif next:
        w_index += 1
        question_word = list_of_en_words[w_index]
    print(list_of_en_words)
    data = {
        'result': result,
        'list_of_ua_words': list_of_ua_words,
        "question_word" : question_word,
    }
    return render(request, 'base_app/training.html', data)