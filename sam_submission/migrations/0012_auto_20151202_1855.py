# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0011_auto_20151202_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='review_count',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='reviewers_count',
        ),
        migrations.AddField(
            model_name='submission',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviewers_count',
            field=models.IntegerField(default=0),
        ),
    ]
