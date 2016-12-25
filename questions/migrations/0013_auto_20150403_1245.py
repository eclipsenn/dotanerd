# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20150403_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(blank=True, to='questions.Tag', null=True, choices=[(1, 2), (3, 4)]),
            preserve_default=True,
        ),
    ]
