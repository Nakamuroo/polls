# Generated by Django 4.1.1 on 2022-12-01 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_question_life_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='life_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 19, 55, 50, 658677), verbose_name='Время жизни'),
        ),
    ]
