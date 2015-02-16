from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import CardAnswerForm, CardScoreForm
from .models import CardAnswer
from .utils import get_or_create_priority_card_answer, get_card_infos


def check(request):
    card_answer = get_or_create_priority_card_answer()
    form = CardAnswerForm(instance=card_answer)
    return render(request, 'cards/check.html', {
        'card': card_answer.card,
        'form': form,
    })


def rate(request):
    card_answer = CardAnswer.objects.get(pk=request.POST.get('id'))
    form = CardAnswerForm(request.POST, instance=card_answer)
    dict = {
        'card': card_answer.card,
        'form': form,
    }
    if not form.is_valid():
        return render(request, 'cards/check.html', dict)
    card_answer.end_time = timezone.now()
    form.save()
    dict['score_form'] = CardScoreForm(instance=card_answer)
    return render(request, 'cards/rate.html', dict)


def finish(request):
    card_answer = CardAnswer.objects.get(pk=request.POST.get('id'))
    score_form = CardScoreForm(request.POST, instance=card_answer)
    if not score_form.is_valid():
        return render(request, 'cards/rate.html', {
            'card': card_answer.card,
            'score_form': score_form,
        })
    return redirect('cards:check')


def all(request):
    return render(request, 'cards/all.html', {'card_infos': get_card_infos()})
