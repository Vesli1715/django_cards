from django.http import HttpResponseRedirect , HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .forms import WordsForm, DeleteForm
from .models import Words

def base(request):
    return render(request,'word_cards/content.html')

def add_words(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = NameForm(request.POST)
        en = request.POST['en_word'].lower()
        ua = request.POST['ua_word'].lower()
        if en.isalpha() and ua.isalpha():
            # process the data in form.cleaned_data as required
            field = WordsForm(request.POST)
            field.save()
            # redirect to a new URL:
            data = {'en': en, 'ua': ua}
            return redirect('word_cards/just_been_added', {'data': data})# must be redirect

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WordsForm()

    return render(request, 'word_cards/add_words.html', {'form': form})

def just_been_added(request):
    return render(request,'word_cards/just_been_added.html')


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
    D = {'form': form, 'fields':fields}
    return render(request, 'word_cards/all_words_list.html', D )

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
    return render(request, 'word_cards/all_words_list.html', data )


def training_flip_cards(request):
    fields = Words.objects.all().order_by('-id')[:10]
    return render(request,'word_cards/training_flip_cards.html',{'fields':fields})

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







