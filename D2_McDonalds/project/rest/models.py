from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

class Staff(models.Model):
		director = 'DI'
		admin = 'AD'
		cook = 'CO'
		cashier = 'CA'
		cleaner = 'CL'

		POSITIONS = [
				(director, 'Директор'),
				(admin, 'Администратор'),
				(cook, 'Повар'),
				(cashier, 'Кассир'),
				(cleaner, 'Уборщик')
		]

		full_name = models.CharField(max_length = 255)
		position = models.CharField(max_length = 255, choices=POSITIONS, default=cashier)
		labor_contract = models.IntegerField()

class Product(models.Model):
		DRINK = 'DRNK'
		BURGER = 'BRGR'
		SNACK = 'SNCK'
		DESSERT = 'DSRT'

		TYPE_CHOICES = [
			 (DRINK, 'Drink'),
			 (BURGER, 'Burger'),
			 (SNACK, 'Snack'),
			 (DESSERT, 'Dessert'),
		]

		type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=BURGER)
		name = models.CharField(max_length = 255)
		price = models.FloatField(default = 0.0, validators=[MinValueValidator(0))
		composition = models.TextField(default = "Состав не указан")
		description = models.TextField()
  
		def __str__(self):
			return f'Product #{self.pk} - Name: {self.name}'
   
class Order(models.Model):
		time_in = models.DateTimeField(auto_now_add = True)
		time_out = models.DateTimeField(null = True)
		cost = models.FloatField(default = 0.0)
		take_away = models.BooleanField(default = False)
		complete = models.BooleanField(default = False)
		staff = models.ForeignKey(Staff, on_delete = models.CASCADE)

		products = models.ManyToManyField(Product, through = 'ProductOrder')

class ProductOrder(models.Model):
		product = models.ForeignKey(Product, on_delete = models.CASCADE)
		order = models.ForeignKey(Order, on_delete = models.CASCADE)
		amount = models.IntegerField(default = 1)

#(venv) ~/django-projects/Mac $ python3 manage.py makemigrations
#(venv) ~/django-projects/Mac $ python3 manage.py migrate