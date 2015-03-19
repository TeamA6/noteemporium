# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(verbose_name=b'19/03/2015 12:49'),
        ),
    ]
