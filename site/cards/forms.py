from django import forms

from .models import CardAnswer


class CardAnswerForm(forms.ModelForm):
    class Meta:
        model = CardAnswer
        fields = ['answer']
