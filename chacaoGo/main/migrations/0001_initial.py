# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('categoryName', models.CharField(max_length=2, choices=[('SE', 'Seguridad'), ('VI', 'Vialidad'), ('DS', 'Deficiencia de Servicios'), ('DE', 'Deportes'), ('CU', 'Cultura'), ('PR', 'Productos'), ('SP', 'Servicios Públicos'), ('DM', 'Deterioro Municipal')])),
                ('eventType', models.CharField(max_length=3, choices=[('ZP', 'Zona Peligrosa'), ('DEL', 'Delito'), ('AS', 'Actividad Sospechosa'), ('AC', 'Accidente'), ('EM', 'Embotellamiento'), ('PV', 'Peligro en la Vía'), ('PR', 'Protesta'), ('AM', 'Asistencia médica'), ('SA', 'Servicio de Agua'), ('SE', 'Servicio Eléctrico'), ('RRS', 'Recolección de Residuos Solidos'), ('MA', 'Maratón'), ('ED', 'Encuentro Deportivo'), ('BA', 'Bailoterapia'), ('YO', 'Yoga'), ('CD', 'Clase Deportiva'), ('CO', 'Concierto'), ('FE', 'Feria'), ('OT', 'Obra de Teatro'), ('EA', 'Exposición de arte'), ('JD', 'Jornada de Documentación'), ('VPE', 'Venta de Producto Escaso'), ('JE', 'Jornada Electoral'), ('DES', 'Descuento'), ('DS', 'Donación de sangre'), ('SM', 'Solicitud de Medicamento'), ('JV', 'Jornada Veterinaria'), ('SV', 'Solicitud de Voluntarios'), ('CA', 'Calles y avenidas'), ('AC', 'Aceras'), ('PC', 'Patrimonio Cultural'), ('TE', 'Terreno')])),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=500)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('xPosition', models.FloatField()),
                ('yPosition', models.FloatField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('vip', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('evenType', models.ForeignKey(to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('userType', models.CharField(max_length=9, choices=[('Usuario', 'Usuario'), ('Moderador', 'Moderador'), ('Alcaldía', 'Alcaldía')], default='Usuario')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to='main.User'),
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
