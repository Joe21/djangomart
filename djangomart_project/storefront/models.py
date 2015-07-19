from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible # For Python 3.4 and 2.7
class Customer(models.Model):
	# Customer model extends from User to handle non auth related info/functionality
	user = models.OneToOneField(User)

	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email_address = models.CharField(max_length=50)
	shipping_address = models.CharField(max_length=80, null=True)
	shipping_zipcode = models.IntegerField(max_length=5, null=True)
	last_login = models.DateTimeField(default=timezone.now())

	LEVELS = (
		(1, 'Regular'),
		(2, 'Silver'),
		(3, 'Gold'),
		(4, 'Platinum'),
		)
	level = models.IntegerField(max_length=1, choices=LEVELS)

	def __str__(self):
		return self.first_name

class Product(models.Model):
	model_number = models.IntegerField(max_length=10, unique=True)
	title = models.CharField(max_length=80)
	description = models.TextField()
	# Remember to remove this and make this a public static image
	image_300x200 = models.CharField(max_length=200, default="http://prairieceramics.com/wpress/here/wp-content/uploads/2013/10/cache/image_coming_soon-300x200.jpg")
	created = models.DateTimeField(default=timezone.now(), blank=True)
	in_stock = models.BooleanField(default=True)
	back_order_till = models.DateField(null=True)

	### Unit price to regular customer
	price_unit_normal = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit price to silver customer
	price_unit_silver = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit price to gold customer
	price_unit_gold = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit price to platinum customer
	price_unit_platinum = models.DecimalField(max_digits=10, decimal_places=2)

	### Shipping price to customers 
	price_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Shipping price to platinum customers
	price_shipping_platinum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	### Total unit price to normal customer
	price_total_normal = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit price to silver customer
	price_total_silver = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit price to gold customer
	price_total_gold = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit price to platinum customer
	price_total_platinum = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit cost to djangomart
	cost_unit = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit shipping cost to djangomart
	cost_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit cost to djangomart
	cost_total = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.title

class Shoppingcart(models.Model):
	# Shoppingcarts can belong to customers if logged in
	customer = models.ForeignKey(Customer, null=True)

	products = models.ManyToManyField(Product)

	checkout = models.BooleanField(default=False)

	def __str__(self):
		return "shopping cart"

class Purchase(models.Model):
	customer = models.ForeignKey(Customer, null=True)

	products = models.ManyToManyField(Product)

	order_number = models.IntegerField(max_length = 10, unique=True)

	bill_to_address = models.CharField(max_length=80, null=True)

	bill_to_zipcode = models.IntegerField(max_length=5, null=True)

	bill_to_cc_number = models.BigIntegerField(max_length=16, null=True)

	ship_to_address = models.CharField(max_length=80, null=True)

	ship_to_zipcode = models.IntegerField(max_length=5, null=True)

	created = models.DateTimeField(default=timezone.now(), blank=True)

	### Choice field for purchase status
	STATUS = (
		(1, 'Processing'),
		(2, 'Shipped'),
		(3, 'Complete'),
		(4, 'Return/Refund'),
		(5, 'Cancelled')
		)
	status = models.IntegerField(max_length=1, choices=STATUS, default=1)

	### Total price of purchase to customer
	price_purchase = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Shipping price of purchase to customer
	price_shipping = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Total price on invoice to customer
	price_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	
	### Total cost of purchase to Thuzio
	cost_purchase = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Shipping cost of purchase to Thuzio
	cost_shipping = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Total cost of purchase to Thuzio
	cost_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Total revenue of purchase to Thuzio
	revenue_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	def __str__(self):
		return "order# {}".format(self.order_number)