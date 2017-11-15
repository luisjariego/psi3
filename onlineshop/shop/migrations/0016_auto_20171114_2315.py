# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-14 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20171110_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='prodSlug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
