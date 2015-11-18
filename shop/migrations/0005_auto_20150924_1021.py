# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20150924_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='locaion',
            new_name='location',
        ),
    ]
