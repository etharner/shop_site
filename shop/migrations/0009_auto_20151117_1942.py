# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20151116_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('bug_url', models.CharField(verbose_name='Адрес доставки', max_length=300)),
                ('bug_desc', models.CharField(verbose_name='Адрес доставки', max_length=1000)),
                ('bug_rate', models.CharField(verbose_name='Адрес доставки', max_length=300)),
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
            name='desc',
            field=models.CharField(verbose_name='Описание товара', max_length=500),
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
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(verbose_name='Адрес доставки', max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(verbose_name='Электронная почта', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(verbose_name='Имя заказчика', max_length=16),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(verbose_name='Фамилия заказчика', max_length=16),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='count',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(to='shop.Item', default=False, verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(to='shop.Order', default=False, verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(verbose_name='Электронная почта', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(verbose_name='Имя пользователя', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(verbose_name='Пароль', max_length=16),
        ),
    ]
