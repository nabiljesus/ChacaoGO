# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150630_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 4, 5, 0, 368022, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 4, 5, 9, 973306, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 4, 5, 24, 476930, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='xPosition',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='yPosition',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 4, 5, 51, 766741, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
