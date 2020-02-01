# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='shortened_url',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]