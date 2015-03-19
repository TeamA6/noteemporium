# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20150319_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(verbose_name=b'19/03/2015 14:47'),
            preserve_default=True,
        ),
    ]
