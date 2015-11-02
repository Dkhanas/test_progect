# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fortest',
            old_name='prosessed',
            new_name='processed',
        ),
        migrations.AlterField(
            model_name='fortest',
            name='name',
            field=models.CharField(unique=True, max_length=b'15'),
        ),
    ]
