from django.db import models


class Words(models.Model):

    en_word = models.CharField(max_length=16)
    ua_word = models.CharField(max_length=16)
    added_data = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.en_word, self.ua_word)
