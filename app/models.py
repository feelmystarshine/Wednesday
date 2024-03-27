from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models. Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
    image = models.ImageField(upload_to ='product')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    upload_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.name} - {self.quantity} pcs"




class Review(models. Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    upload_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)