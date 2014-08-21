# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20140819_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('item', models.ForeignKey(to='shop.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
