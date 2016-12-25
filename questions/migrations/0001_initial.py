# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('a_var', models.CharField(max_length=255)),
                ('b_var', models.CharField(max_length=255)),
                ('c_var', models.CharField(max_length=255)),
                ('d_var', models.CharField(max_length=255)),
                ('correct_var', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
