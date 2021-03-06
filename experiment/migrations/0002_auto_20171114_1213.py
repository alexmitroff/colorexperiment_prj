# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.PositiveIntegerField(default=0, verbose_name='позиция')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.Image')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['stimul', 'user', 'pos'],
            },
        ),
        migrations.RemoveField(
            model_name='stimul',
            name='user',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='art_exp',
            field=models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='художественная подготовка'),
        ),
        migrations.AddField(
            model_name='answer',
            name='stimul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.Stimul'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.UserInfo'),
        ),
    ]
