# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_auto_20171123_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='телефон'),
        ),
    ]
