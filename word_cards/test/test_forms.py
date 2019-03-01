from django.test import TestCase
from word_cards.forms import WordsForm, DeleteForm
from registration.forms import SignupForm

class Setup_Class(TestCase):

    def setUp(self):
        self.words = WordsForm.objects.create(en_word="hello", ua_word="привіт")
        self.delete_word = DeleteForm.objects.create(delete_word='Yarik')
        self.user = SignupForm.objects.create(username='Yarik',
                                              email="john@gmail.com",
                                              password1="password123",
                                              password2="password123")


class WordsForm_Test(TestCase):

    def test_validation_added_words(self):
        forms = WordsForm({'en_word': 'english', 'ua_word': 'ukrainian'})
        self.assertTrue(forms.is_valid())

        record = forms.save(commit=False)
        self.assertEqual(record.en_word, 'english')
        self.assertEqual(record.ua_word, 'ukrainian')


class Word_DeleteForm_Test(TestCase):

    def test_validation_deleting_word(self):
        form = DeleteForm({'delete_word': "word"})
        self.assertTrue(form.is_valid())


class User_SignupForm_Test(TestCase):

    def test_SignupForm_valid(self):
        form = SignupForm(data={'username': "John",
                                'email': "box@gmail.com",
                                'password1': "yarik123456789",
                                'password2': "yarik123456789"})
        self.assertTrue(form.is_valid())
        record = form.save()
        self.assertEqual(record.username, "John")
        self.assertEqual(record.email, "box@gmail.com")


    def test_UserForm_invalid(self):
        form = SignupForm(data={'username': '',
                                'email': "false",
                                'password1': "false",
                                'password2': 'password'})

        self.assertFalse(form.is_valid())
