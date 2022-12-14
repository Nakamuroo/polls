# Generated by Django 4.1.1 on 2022-12-01 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_question_votes_alter_question_life_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='img',
            field=models.ImageField(null=True, upload_to='images/question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='life_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 18, 43, 0, 198451), verbose_name='Время жизни'),
        ),
    ]
