# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catSlug',
            field=models.SlugField(blank=True),
        ),
    ]
