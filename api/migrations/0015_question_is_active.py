# Generated by Django 2.2.10 on 2020-05-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200515_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
