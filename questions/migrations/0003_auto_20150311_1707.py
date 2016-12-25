# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20150311_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
