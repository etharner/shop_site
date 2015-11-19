# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20151119_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(default=False, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', to='shop.Item'),
        ),
    ]
