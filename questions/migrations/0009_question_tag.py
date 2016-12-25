# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20150403_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='questions.Tag'),
            preserve_default=True,
        ),
    ]
