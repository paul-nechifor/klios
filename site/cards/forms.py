from django import forms

from .models import CardAnswer


class CardAnswerForm(forms.ModelForm):
    id = forms.IntegerField(widget = forms.HiddenInput)
    class Meta:
        model = CardAnswer
        fields = ['id', 'answer']
        widgets = {'id': forms.HiddenInput()}


class CardScoreForm(forms.ModelForm):
    id = forms.IntegerField(widget = forms.HiddenInput)
    class Meta:
        model = CardAnswer
        fields = ['id', 'score']
        widgets = {'id': forms.HiddenInput()}

    def clean_score(self):
        score = self.cleaned_data['score']
        if score < 0.0 or score > 1.0:
            raise forms.ValidationError('Score is not in (0.0, 1.0) range.')
        return score
