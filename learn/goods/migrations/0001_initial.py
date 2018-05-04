# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-04 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_title', models.CharField(max_length=40)),
                ('g_img', models.ImageField(upload_to='img_goods')),
                ('g_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('g_delete', models.BooleanField(default=False)),
                ('g_unit', models.CharField(default='500g', max_length=20)),
                ('g_click', models.ImageField(upload_to='')),
                ('g_abstract', models.CharField(max_length=200)),
                ('g_inventory', models.ImageField(upload_to='')),
                ('g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'db_table': 'goods_info',
            },
        ),
    ]