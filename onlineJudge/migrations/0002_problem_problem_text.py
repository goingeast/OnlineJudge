# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('onlineJudge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_text',
            field=models.CharField(default=datetime.datetime(2015, 9, 27, 4, 43, 58, 219683, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
