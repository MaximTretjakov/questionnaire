from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.models import Questionnaire, Question, Choice, Statistics
from api.forms import QuestionnaireForm, QuestionForm


class QuestionUpdateView(ListCreateAPIView):
    """
    функционал админа
    Позволяет изменить вопрос опросника
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated, IsAdminUser,)
    template_name = 'account/question_update_admin.html'

    def get(self, request, *args, **kwargs):
        question_items = Question.objects.all()
        return render(request, self.template_name, {'question_items': question_items})

    def post(self, request, *args, **kwargs):
        upd_question = Question.objects.get(id=request.POST.get('choice'))
        upd_question.question_text = request.POST.get('new_name')
        upd_question.save()
        return HttpResponseRedirect(reverse('api:update_q'))


class QuestionAppendView(ListCreateAPIView):
    """
    функционал админа
    Позволяет добавить вопрос опросника
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated, IsAdminUser,)
    template_name = 'account/question_append_admin.html'

    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})


class QuestionDeleteView(ListCreateAPIView):
    """
    функционал админа
    Позволяет выбрать и удалить вопрос опросника
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated, IsAdminUser,)
    template_name = 'account/question_delete_admin.html'

    def get(self, request, *args, **kwargs):
        question_items = Question.objects.all()
        return render(request, self.template_name, {'question_items': question_items})

    def post(self, request, *args, **kwargs):
        del_question = Question.objects.get(id=request.POST.get('choice', None))
        del_question.delete()
        return HttpResponseRedirect(reverse('api:questionnaire'))


class QuestionnaireUpdateView(ListCreateAPIView):
    """
    функционал админа
    Позволяет изменить опросник
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated, IsAdminUser,)
    template_name = 'account/update_admin.html'

    def get(self, request, *args, **kwargs):
        questionnaire_items = Questionnaire.objects.all()
        return render(request, self.template_name, {'questionnaire_items': questionnaire_items})

    def post(self, request, *args, **kwargs):
        upd_questionnaire = Questionnaire.objects.get(id=request.POST.get('choice'))
        upd_questionnaire.questionnaire_name = request.POST.get('new_name')
        upd_questionnaire.save()
        return HttpResponseRedirect(reverse('api:update'))


class QuestionnaireAppendView(ListCreateAPIView):
    """
    функционал админа
    Позволяет добавить опросник
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated, IsAdminUser,)
    template_name = 'account/append_admin.html'

    def get(self, request, *args, **kwargs):
        form = QuestionnaireForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = QuestionnaireForm(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})


class QuestionnaireDeleteView(ListCreateAPIView):
    """
    функционал админа
    Позволяет выбрать и удалить опросник
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated, IsAdminUser,)
    template_name = 'account/delete_admin.html'

    def get(self, request, *args, **kwargs):
        questionnaire_items = Questionnaire.objects.all()
        return render(request, self.template_name, {'questionnaire_items': questionnaire_items})

    def post(self, request, *args, **kwargs):
        del_questionnaire = Questionnaire.objects.get(id=request.POST.get('choice', None))
        del_questionnaire.delete()
        return HttpResponseRedirect(reverse('api:questionnaire'))


class QuestionnaireListView(APIView):
    """
    Функционал пользователя
    Выводит все опросники
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)
    template_name = 'account/all_questionnaire.html'

    def get(self, request):
        queryset = Questionnaire.objects.all()
        return Response({'queryset': queryset})


class QuestionsListView(APIView):
    """
    Функционал пользователя
    Выводит все вопросы опросника
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)
    template_name = 'account/all_questions.html'

    def get(self, request, questionnaire_id):
        q_id = get_object_or_404(Questionnaire, id=questionnaire_id)
        questions = q_id.question_set.filter(is_active=True)
        if len(questions) == 0:
            for q in q_id.question_set.filter(is_active=False):
                q.is_active = True
                q.save()
            return HttpResponseRedirect(reverse('api:questionnaire'))
        return render(request, 'account/all_questions.html', {'q_id': q_id, 'questions': questions})


class VoteView(APIView):
    """
    Функционал пользователя
    Сохраняет результаты прохождения опроса.
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)
    template_name = 'account/all_questions.html'

    def post(self, request, questionnaire_id, question_id):
        questionnaire_name = Questionnaire.objects.get(id=questionnaire_id).questionnaire_name
        question_name = Question.objects.get(id=question_id)
        question_name.is_active = False
        question_name.save()
        choice_name = Choice.objects.get(id=request.POST.get('choice', True)).choice_text
        statistics = Statistics(user_id=request.user,
                                questionnaire=questionnaire_name,
                                questions=question_name.question_text,
                                choice=choice_name)
        statistics.save()
        return HttpResponseRedirect(reverse('api:questions', args=(questionnaire_id,)))


class ResultsListView(APIView):
    """
    Функционал пользователя
    Отображает результаты пользователя.
    """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)
    template_name = 'account/all_results.html'

    def get(self, request):
        all_results = Statistics.objects.all().filter(user_id=request.user)
        return Response({'all_results': all_results, 'user': request.user})
