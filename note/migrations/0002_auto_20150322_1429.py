# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(verbose_name=b'22/03/2015 14:29'),
            preserve_default=True,
        ),
    ]
