# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthTable',
            fields=[
                ('authenticator', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField()),
                ('user_id', models.ForeignKey(to='first.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
