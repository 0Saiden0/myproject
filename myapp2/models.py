from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    address = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Username: {self.name}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Product: {self.name}'
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    