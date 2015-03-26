# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_reported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='subject',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
