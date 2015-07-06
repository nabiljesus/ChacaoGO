# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(max_length=9, choices=[('Usuario', 'Usuario'), ('Moderador', 'Moderador'), ('Alcaldía', 'Alcaldía')], default='Usuario'),
        ),
    ]
