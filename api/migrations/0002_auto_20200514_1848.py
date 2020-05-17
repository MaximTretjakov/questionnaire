# Generated by Django 2.2.10 on 2020-05-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='text_q',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='type_q',
            field=models.CharField(choices=[('TXT', 'TEXT'), ('ONE', 'ONE'), ('SEV', 'SEVERAL')], default='TXT', max_length=3),
        ),
    ]
