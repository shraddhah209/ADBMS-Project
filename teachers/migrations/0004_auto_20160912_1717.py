# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20160912_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_name',
            field=models.CharField(max_length=70),
        ),
    ]
