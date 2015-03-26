# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20150325_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='reported',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
