# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam_submission', '0012_auto_20151202_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='notification_recip')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='notification_sender')),
            ],
            options={
                'verbose_name': 'User Notification',
            },
        ),
    ]
