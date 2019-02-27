from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    en_word = models.CharField(max_length=30)
    ua_word = models.CharField(max_length=30)
    added_data = models.DateField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.en_word, self.ua_word)
