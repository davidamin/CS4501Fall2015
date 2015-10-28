# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vehicle',
            field=models.ForeignKey(blank=True, to='first.Vehicle'),
            preserve_default=True,
        ),
    ]
