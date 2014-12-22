# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_cardtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardanswer',
            name='answer',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cardanswer',
            name='end_time',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cardanswer',
            name='score',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
