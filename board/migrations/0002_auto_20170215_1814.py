# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_desc',
            field=models.TextField(),
        ),
    ]