# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20150526_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure_Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codes', models.CharField(default=b'0', max_length=200)),
                ('full_name', models.CharField(default=b'', max_length=100)),
                ('abbrev_name', models.CharField(default=b'', max_length=50)),
            ],
        ),
    ]
