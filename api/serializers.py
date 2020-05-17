from rest_framework import serializers
from api.models import Questionnaire, Question


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('name', 'description',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text_q', 'type_q',)
