# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150924_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(verbose_name='Имя пользователя', max_length=16)),
                ('email', models.CharField(verbose_name='Электронная почта', max_length=100)),
                ('password', models.CharField(verbose_name='Пароль', max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='location',
            field=models.CharField(verbose_name='Вложенность', max_length=250),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Название категории', max_length=250),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(to='shop.Category', default=False, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(verbose_name='Название товара', max_length=250),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
    ]
