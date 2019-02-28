from django.test import TestCase
from django.test import Client
from word_cards.forms import WordsForm, DeleteForm
from registration.forms import SignupForm

class Setup_Class(TestCase):

    def setUp(self):
        self.words = WordsForm.objects.create(en_word="hello", ua_word="привіт")
        self.user = SignupForm.objects.create(username='John',
                                              email="john@gmail.com",
                                              password1="password123",
                                              password2="password123")

class User_SignupForm_Test(TestCase):

    def test_SignupForm_valid(self):
        form = SignupForm(data={'username': "John",
                                'email': "box@gmail.com",
                                'password1': "yarik123456789",
                                'password2': "yarik123456789"})

        self.assertTrue(form.is_valid())


    def test_UserForm_invalid(self):
        form = SignupForm(data={'username': '',
                                'email': "false",
                                'password1': "false",
                                'password2': 'password'})
        self.assertFalse(form.is_valid())