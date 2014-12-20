from django.db import models


class CardContent(models.Model):
    front = models.TextField()
    back = models.TextField()


class Card(models.Model):
    content = models.ForeignKey(CardContent)


class CardAnswer(models.Model):
    card = models.ForeignKey(Card)
    answer = models.TextField()
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField()
    score = models.FloatField()
