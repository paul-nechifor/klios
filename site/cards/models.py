from django.db import models


class Card(models.Model):
    pass


class CardTag(models.Model):
    card = models.ForeignKey(Card)
    name = models.CharField(max_length=100)


class CardContent(models.Model):
    card = models.OneToOneField(Card, related_name='content')
    front = models.TextField()
    back = models.TextField()


class CardAnswer(models.Model):
    card = models.ForeignKey(Card)
    answer = models.TextField()
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField()
    score = models.FloatField()
