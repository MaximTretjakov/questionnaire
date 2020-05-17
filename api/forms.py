from django import forms
from django.forms.models import inlineformset_factory
from api.models import Questionnaire, Question

AnswerFormSet = inlineformset_factory(Questionnaire, Question, exclude=('question',), extra=0, can_delete=False)


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ('questionnaire_name',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('questionnaire', 'question_text', )
