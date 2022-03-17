from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class messMenu(models.Model):
    itemName = models.CharField(max_length=25,null=True)
    itemPrice = models.IntegerField(null=True)

class OrderHistory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=25,null=True)
    itemPrice = models.IntegerField(null=True)
    time = models.DateTimeField(null=True)