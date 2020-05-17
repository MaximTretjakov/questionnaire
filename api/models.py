from django.db import models


class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=100)


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Choice(models.Model):
    ChoiceTYPE = (
        ("YES", "YES"),
        ("NO", "NO"),
        ("IDN", "I dont't know"),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type_q = models.CharField(max_length=3, choices=ChoiceTYPE, default='IDN')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Statistics(models.Model):
    user_id = models.CharField(max_length=200, blank=True)
    questionnaire = models.CharField(max_length=200, blank=True)
    questions = models.CharField(max_length=200, blank=True)
    choice = models.CharField(max_length=200, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now=True)
