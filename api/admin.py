from django.contrib import admin
from api.models import Questionnaire, Question, Statistics, Choice


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('questionnaire_name',)
    list_filter = ('questionnaire_name',)
    search_fields = ('questionnaire_name',)


admin.site.register(Questionnaire, QuestionnaireAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'is_active')
    list_filter = ('question_text',)
    search_fields = ('question_text',)


admin.site.register(Question, QuestionAdmin)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'questionnaire', 'questions', 'choice', 'started_at', 'ended_at')
    list_filter = ('user_id',)
    search_fields = ('user_id', 'questionnaire_id')
    ordering = ['user_id']


admin.site.register(Statistics, StatisticsAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'type_q', 'choice_text', 'votes')
    list_filter = ('type_q', 'choice_text')
    search_fields = ('type_q',)
    ordering = ['type_q']


admin.site.register(Choice, ChoiceAdmin)
