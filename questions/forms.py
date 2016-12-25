__author__ = 'eclipse'
from django import forms
from models import Question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['rating', 'total_correct', 'total_incorrect', 'appear_counter']


class QuestionForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id': 'choice'}))

    def __init__(self, custom_choices, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answer'].choices = custom_choices
