# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineJudge', '0003_auto_20150927_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
    ]
