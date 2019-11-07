# Generated by Django 2.2.6 on 2019-11-06 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0015_auto_20191105_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('useramount', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='payno',
            name='useramount',
        ),
        migrations.RemoveField(
            model_name='payno',
            name='userid',
        ),
        migrations.AddField(
            model_name='payno',
            name='paytmno',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamesection',
            name='gamedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 16, 28, 59, 844959)),
        ),
    ]
