# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
