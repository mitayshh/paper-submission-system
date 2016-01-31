# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam_submission', '0005_paper_is_assigned_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('paper_id', models.ForeignKey(to='sam_submission.Paper')),
                ('pcm_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
