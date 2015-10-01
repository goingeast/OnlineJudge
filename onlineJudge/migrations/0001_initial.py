# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('successful_rate', models.IntegerField()),
                ('solution', models.CharField(max_length=500)),
                ('test_cases', models.CharField(max_length=500)),
                ('tag_text', models.CharField(max_length=200)),
            ],
        ),
    ]
