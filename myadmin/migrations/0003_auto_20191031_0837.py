# Generated by Django 2.2.6 on 2019-10-31 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_auto_20191031_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesection',
            name='gamedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 31, 8, 37, 4, 84211)),
        ),
    ]
