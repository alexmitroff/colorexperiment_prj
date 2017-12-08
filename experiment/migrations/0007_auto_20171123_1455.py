# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0006_auto_20171123_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=0, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='art_exp',
            field=models.IntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='художественная подготовка'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='cinema_freq',
            field=models.IntegerField(default=0, help_text='штуки в месяц', verbose_name='частота походов в кинотеатр'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='телефон'),
        ),
    ]