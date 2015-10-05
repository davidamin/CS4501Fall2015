# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='max_seats',
            field=models.IntegerField(null=True, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trunk_space',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
