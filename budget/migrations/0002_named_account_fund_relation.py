# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='budget.Account'),
        ),
    ]
