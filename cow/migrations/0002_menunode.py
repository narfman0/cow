# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('enabled', models.BooleanField(default=True)),
                ('children', models.ManyToManyField(related_name='_menunode_children_+', to='cow.MenuNode')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cow.Page')),
            ],
        ),
    ]
