# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0002_submission_is_requested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='is_requested',
        ),
        migrations.AddField(
            model_name='paper',
            name='is_requested',
            field=models.BooleanField(default=0),
        ),
    ]
