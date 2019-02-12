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


class DeleteForm(forms.Form):
    delete_word = forms.CharField(label='Enter english word you want to delete', max_length=16)


CHOICES=[('select1','select 1'),
         ('select2','select 2')]

class SimpleForm(forms.Form):
    my_choise = forms.ChoiceField(required=False, choices=CHOICES, widget=forms.RadioSelect)



