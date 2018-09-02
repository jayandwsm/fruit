# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-08 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccount', models.IntegerField(db_column='cart_count', verbose_name='数量')),
                ('goods', models.ForeignKey(db_column='goods_id', on_delete=django.db.models.deletion.CASCADE, to='member.Goods')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(max_length=50, verbose_name='订单号')),
                ('orderdetail', models.TextField(verbose_name='订单详情')),
                ('adsname', models.CharField(max_length=30, verbose_name='收件人姓名')),
                ('adsphone', models.CharField(max_length=20, verbose_name='收件人电话')),
                ('ads', models.CharField(max_length=300, verbose_name='地址')),
                ('time', models.DateTimeField(auto_now=True)),
                ('acot', models.IntegerField(verbose_name='总数')),
                ('acount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='总价')),
                ('orderstatus', models.IntegerField(choices=[(1, '未支付'), (2, '已支付'), (3, '订单取消')], default=1, verbose_name='订单状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
        ),
    ]
