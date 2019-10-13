from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=164)
    platform = models.CharField(max_length=64)
    score = models.IntegerField(max_length=10)
    genre = models.CharField(max_length=32)
    editors_choice = models.CharField(max_length=32)
