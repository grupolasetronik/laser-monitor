# Generated by Django 4.1.1 on 2022-09-20 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 19, 30, 55, 790809, tzinfo=datetime.timezone.utc)),
        ),
    ]
