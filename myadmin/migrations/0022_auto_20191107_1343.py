# Generated by Django 2.2.6 on 2019-11-07 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0021_auto_20191107_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesection',
            name='gamedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 7, 13, 43, 32, 963906)),
        ),
    ]
