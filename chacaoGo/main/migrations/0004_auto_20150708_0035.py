# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150707_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='event',
            name='evenType',
            field=models.CharField(max_length=3, choices=[('ZP', 'Zona Peligrosa'), ('DEL', 'Delito'), ('AS', 'Actividad Sospechosa'), ('AC', 'Accidente'), ('EM', 'Embotellamiento'), ('PV', 'Peligro en la Vía'), ('PR', 'Protesta'), ('AM', 'Asistencia médica'), ('SA', 'Servicio de Agua'), ('SE', 'Servicio Eléctrico'), ('RRS', 'Recolección de Residuos Solidos'), ('MA', 'Maratón'), ('ED', 'Encuentro Deportivo'), ('BA', 'Bailoterapia'), ('YO', 'Yoga'), ('CD', 'Clase Deportiva'), ('CO', 'Concierto'), ('FE', 'Feria'), ('OT', 'Obra de Teatro'), ('EA', 'Exposición de arte'), ('JD', 'Jornada de Documentación'), ('VPE', 'Venta de Producto Escaso'), ('JE', 'Jornada Electoral'), ('DES', 'Descuento'), ('DS', 'Donación de sangre'), ('SM', 'Solicitud de Medicamento'), ('JV', 'Jornada Veterinaria'), ('SV', 'Solicitud de Voluntarios'), ('CA', 'Calles y avenidas'), ('AC', 'Aceras'), ('PC', 'Patrimonio Cultural'), ('TE', 'Terreno')]),
        ),
    ]
