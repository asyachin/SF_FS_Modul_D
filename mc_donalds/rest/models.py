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

    def __str__(self):
        return self.full_name


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
   name = models.CharField(
       max_length=255,
       unique=True
       )
   price = models.IntegerField(
       default=0,
       validators=[MinValueValidator(0)],
       )
   description = models.TextField(null=True)
  
   def __str__(self):
       return f'Product #{self.pk} - Name: {self.name}'
    
class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    take_away = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    
    def finish_order(self):
      self.time_out = datetime.now()
      self.complete = True
      self.save()
    
    products = models.ManyToManyField(Product, through = 'ProductOrder')
    
class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    _amount = models.IntegerField(default = 1, db_column = 'amount') 

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()
