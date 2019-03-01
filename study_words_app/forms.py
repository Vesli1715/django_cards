from django import forms
from .models import Words


class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = ['en_word', 'ua_word']
        labels = {
            "en_word": "Слово Aнглійською",
            "ua_word": "Переклад"
        }

        widgets = {
            'en_word': forms.TextInput(),
            'ua_word': forms.TextInput(),
        }

class DeleteForm(forms.Form):
    delete_word = forms.CharField(label='Enter any word you want to delete', max_length=16)




