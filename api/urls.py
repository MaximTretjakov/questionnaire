from django.contrib import admin
from django.urls import path, include
from api.views import (QuestionsListView, VoteView, QuestionnaireListView,
                       ResultsListView, QuestionnaireDeleteView, QuestionnaireAppendView,
                       QuestionnaireUpdateView, QuestionUpdateView, QuestionAppendView, QuestionDeleteView)


urlpatterns = [
    # добавление, удаление, изменение вопросов опросника
    path('<int:question_id>/update-question/', QuestionUpdateView.as_view(), name='update_param_q'),
    path('update-question/', QuestionUpdateView.as_view(), name='update_q'),
    path('append-question/', QuestionAppendView.as_view(), name='append_q'),
    path('get-question/', QuestionDeleteView.as_view(), name='get_q'),
    path('<int:question_id>/delete_question/', QuestionDeleteView.as_view(), name='delete_q'),

    # добавление, удаление, изменение опросника
    path('<int:questionnaire_id>/update-questionnaire/', QuestionnaireUpdateView.as_view(), name='update_param'),
    path('update-questionnaire/', QuestionnaireUpdateView.as_view(), name='update'),
    path('append-questionnaire/', QuestionnaireAppendView.as_view(), name='append'),
    path('get-questionnaire/', QuestionnaireDeleteView.as_view(), name='get'),
    path('<int:questionnaire_id>/delete/', QuestionnaireDeleteView.as_view(), name='delete'),

    # вывод всех опросников, вопросов, вывод результатов, сохранение прохождения опроса пользователем
    path('all-questionnaire/', QuestionnaireListView.as_view(), name='questionnaire'),
    path('<int:questionnaire_id>/', QuestionsListView.as_view(), name='questions'),
    path('<int:questionnaire_id>/questionnaire/<int:question_id>/question/', VoteView.as_view(), name='vote'),
    path('all-results/', ResultsListView.as_view(), name='results'),
]
