# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 2, 36, 12, 388642, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 2, 36, 12, 389751, tzinfo=utc), blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 2, 36, 12, 391998, tzinfo=utc), blank=True),
        ),
    ]
