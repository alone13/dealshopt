# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 02:49
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('taikhoan_id', models.IntegerField(verbose_name='TaiKhoan_Id')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='User_CuaHang_SanPham',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('sanpham_id', models.IntegerField(verbose_name='SanPham_Id')),
                ('tencuahang', models.CharField(max_length=265, verbose_name='TenCuaHang')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'User_CuaHang_SanPham',
            },
        ),
        migrations.CreateModel(
            name='User_TrangThai',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('trangthai', models.BooleanField(verbose_name='TrangThai')),
            ],
            options={
                'db_table': 'User_TrangThai',
            },
        ),
    ]
