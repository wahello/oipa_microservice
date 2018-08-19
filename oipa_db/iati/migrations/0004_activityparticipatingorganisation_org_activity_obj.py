# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0003_auto_20170529_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityparticipatingorganisation',
            name='org_activity_obj',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='participating_activity',
                to='iati.Activity'),
        ),
    ]
