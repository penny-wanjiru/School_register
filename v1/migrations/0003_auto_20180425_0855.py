# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-25 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_remove_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
