# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('vendor', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('score', models.SmallIntegerField()),
                ('performance', models.SmallIntegerField()),
                ('design', models.SmallIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
