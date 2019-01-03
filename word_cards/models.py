from django.db import models
from django.forms import ModelForm

class Words(models.Model):
	ua_word = models.CharField(max_length=12)
	en_word = models.CharField(max_length=12)
	added_data = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.ua_word , self.en_word)



		# return self.ua_word , self.en_word



