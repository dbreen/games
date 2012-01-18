import hashlib
import random

from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=32)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.api_key = hashlib.md5(str(random.random())).hexdigest()
        super(Client, self).save(*args, **kwargs)


class Game(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Score(models.Model):
    game = models.ForeignKey(Game)
    username = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    play_date = models.DateTimeField()

