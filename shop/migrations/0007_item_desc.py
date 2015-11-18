# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20151110_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.CharField(default='', verbose_name='Описание товара', max_length=500),
            preserve_default=False,
        ),
    ]
