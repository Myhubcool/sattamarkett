# Generated by Django 2.2.6 on 2019-10-31 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_auto_20191031_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='triplerate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=10)),
                ('gfirst', models.CharField(max_length=10)),
                ('gfirstp', models.CharField(max_length=10)),
                ('gsecond', models.CharField(max_length=10)),
                ('gsecondp', models.CharField(max_length=10)),
                ('gthird', models.CharField(max_length=10)),
                ('gthirdp', models.CharField(max_length=10)),
                ('gfour', models.CharField(max_length=10)),
                ('gfourp', models.CharField(max_length=10)),
                ('gfive', models.CharField(max_length=10)),
                ('gfivep', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='gamesection',
            name='gamedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 31, 9, 5, 53, 282065)),
        ),
    ]