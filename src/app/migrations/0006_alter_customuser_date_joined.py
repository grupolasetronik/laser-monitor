# Generated by Django 4.1.1 on 2022-09-19 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_parameter_key_alter_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 1, 9, 2, 78491, tzinfo=datetime.timezone.utc)),
        ),
    ]
