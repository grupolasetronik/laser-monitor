# Generated by Django 4.1.1 on 2022-09-19 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 1, 10, 41, 674042, tzinfo=datetime.timezone.utc)),
        ),
    ]
