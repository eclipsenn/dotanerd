# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-09 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_auto_20170207_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo_path',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='/static/images/question.jpg', upload_to='/home/eclipse/Documents/share/dotanerd/files/media/profile_photos'),
        ),
    ]
