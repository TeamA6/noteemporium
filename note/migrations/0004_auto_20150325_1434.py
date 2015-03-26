# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20150325_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='reported',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='subject',
            field=models.CharField(max_length=128),
        ),
    ]
