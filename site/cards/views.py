from django.shortcuts import render

from .models import CardAnswer
from .forms import CardAnswerForm


def check(request):
    card_answer = CardAnswer.get_card_answer()
    form = CardAnswerForm(instance=card_answer)
    return render(request, 'cards/check.html', {
        'card': card_answer.card,
        'form': form
    })


def rate(request):
    pass


def finish(request):
    pass
