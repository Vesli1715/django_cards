from django import forms
from .models import Words

class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = [ 'en_word','ua_word',]
        labels = {
        "en_word":"Слово англійською",
        "ua_word":"Переклад"   
    }

class DeleteForm(forms.Form):
    delete_word = forms.CharField(label='Enter english word you want to delete', max_length=12)