# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20150311_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='total_correct',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='total_incorrect',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
