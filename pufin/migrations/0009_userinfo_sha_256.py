# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pufin', '0008_userinfo_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='SHA_256',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]