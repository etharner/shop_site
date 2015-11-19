# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20151117_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(verbose_name='Адрес пользователя', max_length=300)),
                ('pay_method', models.CharField(verbose_name='Способ оплаты', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='bug',
            name='bug_desc',
            field=models.CharField(verbose_name='Описание ошибки', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bug',
            name='bug_rate',
            field=models.CharField(verbose_name='Критичность ошибки', max_length=300),
        ),
        migrations.AlterField(
            model_name='bug',
            name='bug_url',
            field=models.CharField(verbose_name='Страница с ошибкой', max_length=300),
        ),
    ]
