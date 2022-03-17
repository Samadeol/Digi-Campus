from django.db import models

# Create your models here.

class messMenu(models.Model) :
    itemName = models.CharField(max_length=25)
    itemPrice = models.IntegerField()

class messOrder(models.Model):
    rollno=models.IntegerField()
    orderedName=models.CharField(max_length=25)
    orderedPrice=models.IntegerField()
    orderedDate=models.DateTimeField()