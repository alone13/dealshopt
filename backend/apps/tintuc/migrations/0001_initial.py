# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('danhmuc_id', models.IntegerField(verbose_name='DanhMuc_Id')),
                ('tieude', models.CharField(max_length=265, verbose_name='TieuDe')),
                ('hinhanh', models.CharField(max_length=265, verbose_name='HinhAnh')),
                ('mota', models.CharField(max_length=265, verbose_name='MoTa')),
                ('noidung', models.CharField(max_length=265, verbose_name='NoiDung')),
                ('ngaydang', models.DateField(verbose_name='NgayDang')),
                ('trangthai', models.BooleanField(verbose_name='TrangThai')),
            ],
            options={
                'db_table': 'TinTuc',
            },
        ),
    ]
