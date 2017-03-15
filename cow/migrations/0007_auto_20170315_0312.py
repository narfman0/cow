# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0006_auto_20170306_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('enabled', models.BooleanField(default=True)),
                ('root', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('children', models.ManyToManyField(blank=True, to='cow.Menu')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cow.Page')),
            ],
        ),
        migrations.RemoveField(
            model_name='menunode',
            name='children',
        ),
        migrations.RemoveField(
            model_name='menunode',
            name='page',
        ),
        migrations.DeleteModel(
            name='MenuNode',
        ),
    ]
