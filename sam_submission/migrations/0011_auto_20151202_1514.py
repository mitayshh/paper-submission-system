# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0010_auto_20151202_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcm_requests',
            name='submission',
            field=models.ForeignKey(to='sam_submission.Submission'),
        ),
    ]
