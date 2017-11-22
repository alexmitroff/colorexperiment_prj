# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_image_stimul'),
    ]

    operations = [
        migrations.CreateModel(
            name='StimulType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.PositiveIntegerField(default=0, verbose_name='позиция')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип стимула',
                'verbose_name_plural': 'Типы стимулов',
                'ordering': ['pos'],
            },
        ),
        migrations.AlterModelOptions(
            name='stimul',
            options={'ordering': ['show', 'pos'], 'verbose_name': 'Стимул', 'verbose_name_plural': 'Стимулы'},
        ),
        migrations.AddField(
            model_name='stimul',
            name='stype',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='experiment.StimulType'),
        ),
    ]
