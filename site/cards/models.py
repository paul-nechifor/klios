from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    def __unicode__(self):
        return self.content.front


class CardTag(models.Model):
    card = models.ForeignKey(Card)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class CardContent(models.Model):
    card = models.OneToOneField(Card, related_name='content')
    front = models.TextField()
    back = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.front


class CardAnswer(models.Model):
    card = models.ForeignKey(Card)
    answer = models.TextField(blank=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(null=True)
    score = models.FloatField(null=True, default=0)

    def __unicode__(self):
        return '{} {}'.format(self.card.content.front, self.start_time)
