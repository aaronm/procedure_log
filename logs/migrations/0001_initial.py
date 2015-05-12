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
                ('full_name', models.CharField(max_length=100)),
                ('abbrev_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mrn', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('fluoro_time', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('attending', models.ForeignKey(to='logs.Attending')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure_Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=10)),
                ('inpatient', models.IntegerField(default=0)),
                ('outpatient', models.IntegerField(default=1)),
                ('procedure', models.ForeignKey(to='logs.Procedure')),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('abbrev_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='trainee',
            field=models.ForeignKey(to='logs.Trainee'),
        ),
    ]
