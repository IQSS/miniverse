# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datasets', '0004_auto_20160628_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Name of the dataset version', max_length=255)),
                ('slug', models.SlugField(help_text='Auto-filld on save.', max_length=255)),
                ('semantic_version', models.CharField(help_text='Auto-filled on save.  Canonical version number.  e.g. 1.0, 1.5, 2.0, 2.4, etc', max_length=20)),
                ('dset_version_id', models.IntegerField(blank=True, help_text='Auto-filled on save.', null=True)),
                ('doc', jsonfield.fields.JSONField()),
                ('dataset_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.DatasetVersion')),
            ],
        ),
    ]