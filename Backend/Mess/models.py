from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class messMenu(models.Model) :
    itemName = models.CharField(max_length=25)
    itemPrice = models.IntegerField()

class messOrder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    rollno=models.IntegerField()
    
    orderedDate=models.DateTimeField()
    item_1=models.TextField(null=True)
    quantity_1=models.IntegerField(null=True,default=0)
    price_1=models.IntegerField(null=True,default=0)
    item_2=models.TextField(null=True)
    quantity_2=models.IntegerField(null=True,default=0)
    price_2=models.IntegerField(null=True,default=0)
    item_3=models.TextField(null=True)
    quantity_3=models.IntegerField(null=True,default=0)
    price_3=models.IntegerField(null=True,default=0)
    item_4=models.TextField(null=True)
    quantity_4=models.IntegerField(null=True,default=0)
    price_4=models.IntegerField(null=True,default=0)
    item_5=models.TextField(null=True)
    quantity_5=models.IntegerField(null=True,default=0)
    price_5=models.IntegerField(null=True,default=0)
    item_6=models.TextField(null=True)
    quantity_6=models.IntegerField(null=True,default=0)
    price_6=models.IntegerField(null=True,default=0)
  
    time=models.TimeField(null=True)