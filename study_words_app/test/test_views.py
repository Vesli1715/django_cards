from django.test import Client
from django.test import TestCase
from registration.forms import SignupForm




class Test_AddWords_And_Table(TestCase):

    def test_tabel_words(self):
        c = Client()
        response = c.post('/words/table_of_words/', {'en_word': 'john', 'ua_word': 'smithss'})
        self.assertEqual(response.status_code, 200)

