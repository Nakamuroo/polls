# Generated by Django 4.1.1 on 2022-12-01 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_question_description2_alter_question_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='life_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 19, 13, 38, 263285), verbose_name='Время жизни'),
        ),
    ]