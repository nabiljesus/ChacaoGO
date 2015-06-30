# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seiso',
            field=models.CharField(default='mucho', max_length=11),
            preserve_default=False,
        ),
    ]
