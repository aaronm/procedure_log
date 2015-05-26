# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attending',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100, null=True, blank=True)),
                ('abbrev_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mrn', models.CharField(default=b'', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('fluoro_time', models.IntegerField(default=0, null=True, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('duration', models.DurationField(null=True, blank=True)),
                ('mrn', models.CharField(default=b'', max_length=30)),
                ('tech', models.CharField(default=b'', max_length=20)),
                ('location', models.CharField(default=b'', max_length=10)),
                ('inpatient', models.IntegerField(default=0)),
                ('outpatient', models.IntegerField(default=1)),
                ('attending', models.ForeignKey(blank=True, to='logs.Attending', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure_Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(default=0)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('procedure', models.ForeignKey(blank=True, to='logs.Procedure', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100, null=True, blank=True)),
                ('abbrev_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='trainee',
            field=models.ForeignKey(blank=True, to='logs.Trainee', null=True),
        ),
    ]
