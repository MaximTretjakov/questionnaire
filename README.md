# questionnaire
<dl>
<dt>Опросник.</dt>
</dl>

Python 3.7.5
Django 2.2.10
djangorestframework 3.11.0


Как развернуть :

1. git clone https://github.com/MaximTretjakov/questionnaire.git

2. pip install -r requirements.txt

3. python manage.py runserver

4. перейдите по адресу http://127.0.0.1:8000/ в вашем браузере.

Документация по API :

    POST <int:question_id>/update-question/ - обновление вопроса
    POST append-question/ - добавление вопроса
    POST <int:question_id>/delete_question/ - удаление опроса

    POST update-questionnaire/ - обновление опросника
    POST append-questionnaire/ - добавление опросника
    POST <int:questionnaire_id>/delete/ - обновление опросника

    GET all-questionnaire/ - получение всех опросников
    GET <int:questionnaire_id>/ - получение всех вопросов опросника
    POST <int:questionnaire_id>/questionnaire/<int:question_id>/question/ - прохождение опроса и сохранение результатов
    GET all-results/ - получение результатов

    авторизация в системе - реализована через Django authentication framework

Что не смог сделать :

    Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов
    В API передаётся числовой ID пользователя - реализовано через логин пользователя
    Есть некоторая избыточность.