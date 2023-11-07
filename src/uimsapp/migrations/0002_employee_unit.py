# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uimsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='unit',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Human resource', b'Human resource'), (b'Accounts', b'Accounts'), (b'Administration', b'Administration'), (b'Communication', b'Communication'), (b'Records', b'Records'), (b'Stores', b'Stores'), (b'Support staff', b'Support staff')]),
        ),
    ]
