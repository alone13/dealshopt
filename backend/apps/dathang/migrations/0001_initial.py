# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-12 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CTDonHang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('sanpham_id', models.IntegerField(verbose_name='SanPham')),
                ('gia', models.FloatField(verbose_name='Gia')),
                ('thanhtien', models.FloatField(verbose_name='ThanhTien')),
            ],
            options={
                'db_table': 'CTDonHang',
            },
        ),
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('ngaydat', models.DateField(verbose_name='NgayDat')),
                ('trangthai', models.BooleanField(verbose_name='DonHang')),
            ],
            options={
                'db_table': 'DonHang',
            },
        ),
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('tenkhachhang', models.CharField(max_length=265, verbose_name='TenKhachHang')),
                ('diachi', models.CharField(max_length=265, verbose_name='DiaChi')),
                ('email', models.CharField(max_length=265, verbose_name='Email')),
                ('sdt', models.IntegerField(max_length=265, verbose_name='SDT')),
            ],
            options={
                'db_table': 'KhachHang',
            },
        ),
        migrations.AddField(
            model_name='donhang',
            name='khachhang_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dathang.KhachHang'),
        ),
        migrations.AddField(
            model_name='ctdonhang',
            name='donhang_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dathang.DonHang'),
        ),
    ]
