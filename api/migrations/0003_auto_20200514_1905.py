# Generated by Django 2.2.10 on 2020-05-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200514_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='text_q',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='type_q',
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Questionnaire'),
        ),
    ]
