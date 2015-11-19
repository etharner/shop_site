# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pay_method',
            field=models.CharField(default='', max_length=50, verbose_name='Способ оплаты'),
            preserve_default=False,
        ),
    ]
