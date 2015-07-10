# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150709_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('event', models.ForeignKey(to='main.Event')),
                ('user', models.ForeignKey(to='main.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set([('user', 'event')]),
        ),
    ]
