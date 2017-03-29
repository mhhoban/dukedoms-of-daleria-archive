# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 04:18
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=b'')),
                ('type', models.TextField(default=b'')),
                ('cost', models.IntegerField(default=0)),
                ('treasure', models.IntegerField(default=0)),
                ('victory_points', models.IntegerField(default=0)),
                ('actions', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
