import random

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
    answer = models.TextField(blank=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(null=True)
    score = models.FloatField(null=True)

    def __unicode__(self):
        return '{} {}'.format(self.card.content.front, self.start_time)

    @classmethod
    def get_card_answer(cls):
        try:
            card_answer = CardAnswer.objects.get(end_time=None)
        except CardAnswer.DoesNotExist:
            card = random.choice(Card.objects.all())
            card_answer = CardAnswer.objects.create(card=card)
            card_answer.save()
        return card_answer
