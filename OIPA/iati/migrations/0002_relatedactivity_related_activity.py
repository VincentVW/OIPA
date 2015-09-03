# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedactivity',
            name='related_activity',
            field=models.ForeignKey(related_name='related_activity', to='iati.Activity', null=True),
        ),
    ]