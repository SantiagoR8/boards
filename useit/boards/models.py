from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=60)
	isPrivate = models.BooleanField()
	owner = models.ForeignKey(get_user_model(), null=False, related_name='boards', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name}'

class Note(models.Model):
	title = models.CharField(max_length=20)
	text = models.CharField(max_length=100)
	owner = models.ForeignKey(get_user_model(), null=False, related_name='notes', on_delete=models.CASCADE)
	board = models.ForeignKey(Board, null=False, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title} {self.text}'
