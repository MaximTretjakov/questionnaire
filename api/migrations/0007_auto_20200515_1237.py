# Generated by Django 2.2.10 on 2020-05-15 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200515_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='text_q',
            new_name='text_question',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='questionnaire',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='type_q',
        ),
    ]
