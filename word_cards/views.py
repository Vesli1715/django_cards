from random import shuffle
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WordsForm, DeleteForm
from .models import Words



"""---------------- ADD WORDS, TABLE AND DELETING WORDS BLOCK--------------------------"""


@login_required
def add_new_words(request):
    """Function get from the user data of new English and Ukrainian words,
     and write them in db. Also doing some validation of this data, and
     return error message when data is not valid"""

    if request.method == 'POST':
        form = WordsForm(request.POST)
        en = request.POST['en_word']
        ua = request.POST['ua_word']
        if form.is_valid() and (en.isalpha() and ua.isalpha()):
            en_word = form.cleaned_data['en_word'].capitalize()
            ua_word = form.cleaned_data['ua_word'].capitalize()
            form = WordsForm({'en_word': en_word, 'ua_word': ua_word}) #form = WordsForm(request.POST)
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('base_app/word_added_successfully')  # always must be redirect
        else:
            form = WordsForm()
            error_message = True
            return render(request, 'base_app/add_new_words.html', {'form': form, 'error_message': error_message})
    else:
        form = WordsForm()
    return render(request, 'base_app/add_new_words.html', {'form': form})


def word_added_successfully(request):
    """Function return success page, when forms in function add_new_words we get new data"""
    return render(request, 'base_app/word_added_successfully.html')


def logged_in_user_id(request):
    """"Function used in table_of_words()"""
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    return user_id


def table_of_words(request):
    """Function return data from model in table
    and works with DeleteForm for delete record from table"""

    fields = Words.objects.filter(author_id=logged_in_user_id(request)).order_by('-id')
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            word = request.POST.get('delete_word', 'error')
            if word:
                Words.objects.filter(en_word=word).delete()
                Words.objects.filter(ua_word=word).delete()
            D = {'form': form, 'fields': fields}
            return render(request, 'base_app/table_of_words.html', D)
    else:
        form = DeleteForm()
    D = {'form': form, 'fields': fields}
    return render(request, 'base_app/table_of_words.html', D)


""" ---------- TRAINING BLOCK ------------- """

def main_training_page(request):
    """Call the main navigation page of training block"""
    return render(request, 'base_app/main_training_page.html')


def flash_cards(request):
    """Passes english words and translation into flashcard training page"""
    fields = Words.objects.all().order_by('-id')[:8]
    return render(request, 'base_app/flash_cards.html', {'fields': fields})


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
    Used dictionaries (keys -> value) logic when it is compared whether the answer is correct"""

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
        "question_word": question_word,
    }
    return render(request, 'base_app/training.html', data)