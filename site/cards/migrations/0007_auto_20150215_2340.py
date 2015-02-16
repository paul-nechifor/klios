# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20141226_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardanswer',
            name='card',
            field=models.ForeignKey(related_name='answers', to='cards.Card'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cardanswer',
            name='score',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
    ]
