# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0007_auto_20151201_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='is_requested',
        ),
        migrations.AddField(
            model_name='requests',
            name='is_approved',
            field=models.BooleanField(default=0),
        ),
    ]
