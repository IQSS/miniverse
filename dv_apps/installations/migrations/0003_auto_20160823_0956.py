# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0002_auto_20160726_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='installation',
            name='marker',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
