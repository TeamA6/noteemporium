# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='ModuleSubject',
            new_name='sub',
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(verbose_name=b'19/03/2015 14:43'),
            preserve_default=True,
        ),
    ]
