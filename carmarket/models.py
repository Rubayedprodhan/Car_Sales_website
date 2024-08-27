from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Brand(models.Model):
    name=models.CharField(max_length=50)

    def __self__(self):
        return self.name
    
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media/cars')

    def __self__(self):
        return f"{self.brand} {self.title}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.title}"

class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comments by {self.name}"