# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urun', '0003_auto_20170730_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='design',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='performance',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12)]),
        ),
    ]
