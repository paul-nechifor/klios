import random

from models import CardAnswer, Card


def get_or_create_priority_card_answer():
    try:
        return CardAnswer.objects.get(end_time=None)
    except CardAnswer.DoesNotExist:
        card = _get_priority_card()
        card_answer = CardAnswer.objects.create(card=card)
        card_answer.save()
        return card_answer


def get_card_infos():
    return (get_card_info(x) for x in Card.objects.all())


def get_card_info(card):
    n_answers = card.answers.count()
    n_correct = sum(1 for x in card.answers.all() if x.score >= 0.8)
    return {
        'card': card,
        'n_answers': n_answers,
        'n_correct': n_correct,
        'n_wrong':  n_answers - n_correct,
    }


def _get_priority_card():
    # This is a terible way of doing it.
    box_scores = [1000, 500, 100, 50, 10]
    n_boxes = len(box_scores)
    card_boxes = {card.pk: 0 for card in Card.objects.all()}
    for answer in CardAnswer.objects.all():
        n = card_boxes[answer.card.pk]
        if answer.score >= 0.8:
            if n > 0:
                n -= 1
        else:
            if n < n_boxes - 1:
                n += 1
        card_boxes[answer.card.pk] = n

    list = []
    sum = 0
    for card_pk, box_id in card_boxes.items():
        score = box_scores[box_id]
        list.append((score, card_pk))
        sum += score
    choice = random.random() * sum
    running_sum = 0
    for score, card_pk in list:
        running_sum += score
        if running_sum >= choice:
            return Card.objects.get(pk=card_pk)
    raise Exception('This should not happen.')
