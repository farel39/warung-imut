from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  
    price = models.IntegerField()  
    description = models.TextField()  
    stock = models.IntegerField()
    imutness_rating = models.FloatField()

