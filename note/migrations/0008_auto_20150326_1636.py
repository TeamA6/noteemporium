# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_auto_20150326_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='module',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
