# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 22:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pufin', '0006_auto_20170322_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Orig_Loandate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Published',
            field=models.IntegerField(),
        ),
    ]