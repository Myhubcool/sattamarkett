# Generated by Django 2.2.6 on 2019-10-31 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20191031_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umanagedata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 31, 9, 11, 58, 917975)),
        ),
    ]
