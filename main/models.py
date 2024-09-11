from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)  
    price = models.IntegerField()  
    description = models.TextField()  
    stock = models.IntegerField()
    imutness_rating = models.FloatField()

