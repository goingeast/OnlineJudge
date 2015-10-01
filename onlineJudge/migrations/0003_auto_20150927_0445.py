# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineJudge', '0002_problem_problem_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='successful_rate',
            field=models.IntegerField(default=0),
        ),
    ]
