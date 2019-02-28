from django.test import TestCase
from django.test import Client
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
    pass


class Word_DeleteForm_Test(TestCase):

    def test_validation_deleting_word(self):
        form = DeleteForm({'delete_word': "word"})
        self.assertTrue(form.is_valid())

    def test_max_length_of_delete_word(self):
        max_length = DeleteForm._meta.get_field('delete_word').max_length
        self.assertEquals(max_length, 30)






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
        self.assertEqual(record.password1, "yarik123456789")
        self.assertEqual(record.password2, "yarik123456789")

    def test_UserForm_invalid(self):
        form = SignupForm(data={'username': '',
                                'email': "false",
                                'password1': "false",
                                'password2': 'password'})
        self.assertFalse(form.is_valid())