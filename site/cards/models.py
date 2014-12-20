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

    def __unicode__(self):
        return self.front

class CardAnswer(models.Model):
    card = models.ForeignKey(Card)
    answer = models.TextField()
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField()
    score = models.FloatField()

    def __unicode__(self):
        return '{} {}: {}'.format(card.content.front, start_time, answer)
