# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-pub_date']},
        ),
    ]
