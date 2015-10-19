# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('leave_time', models.DateTimeField(blank=True)),
                ('arrive_time', models.DateTimeField(blank=True)),
                ('destination', models.CharField(blank=True, max_length=30)),
                ('start', models.CharField(blank=True, max_length=30)),
                ('comments', models.CharField(blank=True, max_length=300)),
                ('max_miles_offroute', models.FloatField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(unique=True, max_length=24)),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=10)),
                ('payment_type', models.IntegerField(blank=True)),
                ('gender', models.BooleanField(default=False)),
                ('license_number', models.CharField(blank=True, max_length=20)),
                ('age', models.IntegerField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('max_seats', models.IntegerField(default=0, null=True)),
                ('trunk_space', models.FloatField(default=0.0)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('condition', models.CharField(blank=True, max_length=100)),
                ('make', models.CharField(blank=True, max_length=30)),
                ('model', models.CharField(blank=True, max_length=30)),
                ('year', models.IntegerField(default=0)),
                ('color', models.CharField(blank=True, max_length=15)),
                ('plates', models.CharField(blank=True, max_length=10)),
                ('uninsured', models.BooleanField(default=False)),
                ('road_assistance', models.CharField(blank=True, max_length=30)),
                ('accomodations', models.CharField(blank=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='vehicle',
            field=models.ForeignKey(to='first.Vehicle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ride',
            name='car',
            field=models.ForeignKey(to='first.Vehicle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(to='first.User'),
            preserve_default=True,
        ),
    ]
