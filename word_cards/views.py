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


# bad decision 
def show_all_words_list(request):
    fields = Words.objects.all().order_by('-id')
    return render(request, 'word_cards/all_words_list.html', {'fields': fields})


def show_last_ten(request, numb=10):
    fields = Words.objects.all().order_by('-id')[:numb]
    return render(request, 'word_cards/all_words_list.html', {'fields': fields})


def show_last_twenty(request, numb=20):
    fields = Words.objects.all().order_by('-id')[:numb]
    return render(request, 'word_cards/all_words_list.html', {'fields': fields})


def show_last_fifty(request, numb=50):
    fields = Words.objects.all().order_by('-id')[:numb]
    return render(request, 'word_cards/all_words_list.html', {'fields': fields})
# to here


def show_record_data(request):
    en = request.POST['english_word']
    ua = request.POST['ukrainian_word']
    data = {'en': en, 'ua': ua}
    return render(request, 'word_cards/all_words_list.html', data)


def training_flip_cards(request):
    fields = Words.objects.all().order_by('-id')[:10]
    return render(request,'word_cards/training_flip_cards.html',{'fields': fields})

from random import shuffle
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

def index(request):
    query = list(Words.objects.all().order_by('-id')[:5])

    L = []
    for items in query:
        s = str(items)
        words = s.split(' ')
        L.append(words)

    all_words = {key: value for (key, value) in L}

    en_words = []
    ua_words = []
    for en, ua in all_words.items():
        en_words.append(en)
        ua_words.append(ua)

    en_1 = en_words[0]
    en_2 = en_words[1]
    en_3 = en_words[2]
    en_4 = en_words[3]
    en_5 = en_words[4]

    z = ''
    if request.method == 'GET':
        d= dict(request.GET)
        for k,v in d.items():
            print(k)
            z = k


    if all_words[en_1] == z:
        print('success')
    else:
        print("False")
    data = {
        'en_words': en_words,
        'ua_words': ua_words,
        'en_words_1': en_1,
        'en_words_2': en_2,
        'en_words_3': en_3,
        'en_words_4': en_4,
        'en_words_5': en_5,
        'all_words': all_words
    }

    return render(request, 'word_cards/test_polls.html', data)

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


def training(request):
    query = list(Words.objects.all().order_by('-id')[:5])

    L = []
    for items in query:
        s = str(items)
        words = s.split(' ')
        L.append(words)

    all_words = {key: value for (key, value) in L}

    en_words = []
    ua_words = []
    for en, ua in all_words.items():
        en_words.append(en)
        ua_words.append(ua)

    en_1 = en_words[0]
    en_2 = en_words[1]
    en_3 = en_words[2]
    en_4 = en_words[3]
    en_5 = en_words[4]

    z = ''
    if request.method == 'GET':
        d = dict(request.GET)
        for k, v in d.items():
            print(v[0])
            z = v[0]

    if all_words[en_1] == z:
        print('success')
    else:
        print("False")
    data = {
        'en_words': en_words,
        'ua_words': ua_words,
        'en_words_1': en_1,
        'en_words_2': en_2,
        'en_words_3': en_3,
        'en_words_4': en_4,
        'en_words_5': en_5,
        'all_words': all_words
    }
    print()
    return render(request, 'base_app/training.html', data)