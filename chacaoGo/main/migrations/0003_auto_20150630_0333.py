# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_seiso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='seiso',
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(max_length=30),
        ),
    ]
