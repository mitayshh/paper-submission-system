# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0006_requests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='paper_id',
            new_name='paper',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='pcm_id',
            new_name='pcm',
        ),
    ]
