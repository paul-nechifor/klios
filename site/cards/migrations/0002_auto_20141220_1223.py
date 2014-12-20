# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='content',
        ),
        migrations.AddField(
            model_name='cardcontent',
            name='card',
            field=models.OneToOneField(related_name='content', default=None, to='cards.Card'),
            preserve_default=False,
        ),
    ]
