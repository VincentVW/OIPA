# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0005_auto_20150905_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geographicexactness',
            name='category',
        ),
        migrations.RemoveField(
            model_name='geographicexactness',
            name='url',
        ),
    ]