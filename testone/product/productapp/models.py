from django.db import models
from django.http import JsonResponse


class Product(models.Model):
    prodId = models.CharField(max_length=50, primary_key=True)
    category = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    imageId = models.CharField(max_length=50)
    price = models.IntegerField()
    productName = models.CharField(max_length=100)
    subCategory = models.CharField(max_length=100)
    tax = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.productName

class OrderCreation(models.Model):
    orderId = models.CharField(max_length=50, primary_key=True)
    comments = models.TextField()
    contactNumber = models.CharField(max_length=20)
    contactPerson = models.CharField(max_length=100)
    customerId = models.CharField(max_length=50)
    deliveryAddress = models.TextField()
    deliveryLocation = models.CharField(max_length=100)
    orderDate = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    total = models.FloatField()

    def __str__(self):
        return f"order {self.order_id}"
