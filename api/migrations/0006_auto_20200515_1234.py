# Generated by Django 2.2.10 on 2020-05-15 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200515_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='type_q',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO'), ('IDN', "I dont't know")], default='IDN', max_length=3),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_q', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO'), ('IDN', "I dont't know")], default='IDN', max_length=3)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Questions')),
            ],
        ),
    ]