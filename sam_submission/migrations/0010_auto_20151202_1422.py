# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam_submission', '0009_auto_20151202_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='PCM_Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('review', models.FileField(upload_to='reviews', blank=True, null=True)),
                ('reviewed_completed', models.BooleanField(default=0)),
                ('paper_id', models.ForeignKey(to='sam_submission.Paper')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Requests',
            new_name='PCM_Requests',
        ),
        migrations.RemoveField(
            model_name='review',
            name='paper_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.RenameField(
            model_name='pcm_requests',
            old_name='paper',
            new_name='submission',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
