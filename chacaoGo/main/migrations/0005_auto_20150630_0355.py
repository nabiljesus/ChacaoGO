# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='main.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='main.User'),
        ),
    ]
