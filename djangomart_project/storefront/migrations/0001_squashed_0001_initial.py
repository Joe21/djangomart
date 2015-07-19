# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'storefront', '0001_initial')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=50)),
                ('shipping_address', models.CharField(max_length=80, null=True)),
                ('shipping_zipcode', models.IntegerField(max_length=5, null=True)),
                ('last_login', models.DateTimeField(default=datetime.datetime(2015, 7, 19, 2, 32, 54, 746574, tzinfo=utc))),
                ('level', models.IntegerField(max_length=1, choices=[(1, b'Regular'), (2, b'Silver'), (3, b'Gold'), (4, b'Platinum')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_number', models.IntegerField(unique=True, max_length=10)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('image_300x200', models.CharField(default=b'http://prairieceramics.com/wpress/here/wp-content/uploads/2013/10/cache/image_coming_soon-300x200.jpg', max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 7, 19, 2, 32, 54, 747677, tzinfo=utc), blank=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('back_order_till', models.DateField(null=True)),
                ('price_unit_normal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit_silver', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit_gold', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit_platinum', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_shipping_platinum', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('price_total_normal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total_silver', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total_gold', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total_platinum', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_unit', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.IntegerField(unique=True, max_length=10)),
                ('bill_to_address', models.CharField(max_length=80, null=True)),
                ('bill_to_zipcode', models.IntegerField(max_length=5, null=True)),
                ('bill_to_cc_number', models.BigIntegerField(max_length=16, null=True)),
                ('ship_to_address', models.CharField(max_length=80, null=True)),
                ('ship_to_zipcode', models.IntegerField(max_length=5, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 7, 19, 2, 32, 54, 750203, tzinfo=utc), blank=True)),
                ('status', models.IntegerField(default=1, max_length=1, choices=[(1, b'Processing'), (2, b'Shipped'), (3, b'Complete'), (4, b'Return/Refund'), (5, b'Cancelled')])),
                ('price_purchase', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('price_shipping', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('price_total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cost_purchase', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cost_shipping', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cost_total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('revenue_total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('customer', models.ForeignKey(to='storefront.Customer', null=True)),
                ('products', models.ManyToManyField(to=b'storefront.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Shoppingcart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkout', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(to='storefront.Customer', null=True)),
                ('products', models.ManyToManyField(to=b'storefront.Product')),
            ],
        ),
    ]
