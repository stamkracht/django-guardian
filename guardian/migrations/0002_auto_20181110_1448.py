# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 13:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guardian', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupobjectpermission',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=getattr(settings, 'AUTH_GROUP_MODEL', 'auth.Group')),
        ),
    ]
