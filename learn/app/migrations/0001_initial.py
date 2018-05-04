# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-04 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('s_pwd', models.CharField(max_length=30)),
                ('s_email', models.CharField(max_length=30)),
                ('s_addressee', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'freshuser',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_addr', models.CharField(max_length=80)),
                ('u_zip_code', models.CharField(max_length=10)),
                ('u_name', models.CharField(max_length=20)),
                ('u_phone', models.CharField(max_length=20)),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
