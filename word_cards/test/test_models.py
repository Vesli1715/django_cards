from django.test import TestCase
from word_cards.models import Words
from django.contrib.auth.models import User


class WordsModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        """"Run once to set up non-modified data for all class methods.
        Set up non-modified objects used by all test methods"""
        user = User.objects.create()
        Words.objects.create(en_word="Python", ua_word="Пітон", author=user)

    def setUp(self):
        """Run once for every test method to setup clean data. """
        pass

    def test_en_word_label(self):
        words = Words.objects.get(id=1)
        field_label = words._meta.get_field('en_word').verbose_name
        self.assertEqual(field_label, 'en word')

    def test_ua_word_label(self):
        words = Words.objects.get(id=1)
        field_label = words._meta.get_field('ua_word').verbose_name
        self.assertEqual(field_label, 'ua word')

    def test_added_data_lable(self):
        words = Words.objects.get(id=1)
        field_label = words._meta.get_field('added_data').verbose_name
        self.assertEqual(field_label, 'added data')


    def test_en_word_value(self):
        words = Words.objects.get(id=1)
        field_label = words.en_word
        self.assertEqual(field_label, 'Python')

    def test_ua_word_value(self):
        words = Words.objects.get(id=1)
        field_label = words.ua_word
        self.assertEqual(field_label, 'Пітон')


    def test_object_words_equal_en_word_and_ua_word(self):
        words = Words.objects.get(id=1)
        expected_object_words = '%s %s' % (words.en_word, words.ua_word)
        self.assertEquals(expected_object_words, str(words))


    def test_en_word_max_length(self):
        words = Words.objects.get(id=1)
        max_length = words._meta.get_field('en_word').max_length
        self.assertEquals(max_length, 16)

    def test_ua_word_max_length(self):
        words = Words.objects.get(id=1)
        max_length = words._meta.get_field('ua_word').max_length
        self.assertEquals(max_length, 16)
