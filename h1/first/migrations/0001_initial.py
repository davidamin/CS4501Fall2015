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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('leave_time', models.DateTimeField(blank=True)),
                ('arrive_time', models.DateTimeField(blank=True)),
                ('destination', models.CharField(max_length=30, blank=True)),
                ('start', models.CharField(max_length=30, blank=True)),
                ('comments', models.CharField(max_length=300, blank=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=18)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=10)),
                ('payment_type', models.IntegerField(blank=True)),
                ('payment_string', models.CharField(max_length=100, blank=True)),
                ('gender', models.BooleanField(default=False)),
                ('license_number', models.CharField(max_length=20, blank=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('max_seats', models.IntegerField(blank=True)),
                ('trunk_space', models.FloatField(blank=True)),
                ('notes', models.CharField(max_length=500, blank=True)),
                ('condition', models.CharField(max_length=100, blank=True)),
                ('make', models.CharField(max_length=30, blank=True)),
                ('model', models.CharField(max_length=30, blank=True)),
                ('year', models.IntegerField(blank=True)),
                ('color', models.CharField(max_length=15, blank=True)),
                ('plates', models.CharField(max_length=10, blank=True)),
                ('uninsured', models.BooleanField(default=False)),
                ('road_assistance', models.CharField(max_length=30, blank=True)),
                ('accomodations', models.CharField(max_length=30, blank=True)),
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
