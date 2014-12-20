# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20141220_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('card', models.ForeignKey(to='cards.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
