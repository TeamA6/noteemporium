# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20150319_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='ModuleSubject',
            new_name='sub',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(verbose_name=b'19/03/2015 13:56'),
            preserve_default=True,
        ),
    ]
