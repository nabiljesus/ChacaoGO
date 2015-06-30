# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('fullname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('userType', models.CharField(max_length=11)),
            ],
        ),
    ]
