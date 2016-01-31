# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam_submission', '0008_auto_20151201_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewAssignments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_reviewed', models.BooleanField(default=0)),
                ('pcm', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='paper',
            name='is_assigned_to',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='paper',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='reviewers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewed_completed',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='submission',
            name='isReviewed',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='reviewassignments',
            name='submission',
            field=models.ForeignKey(to='sam_submission.Submission'),
        ),
    ]
