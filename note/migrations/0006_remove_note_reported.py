# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20150325_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='reported',
        ),
    ]
