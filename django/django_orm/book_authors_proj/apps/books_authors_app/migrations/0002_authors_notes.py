# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-19 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]