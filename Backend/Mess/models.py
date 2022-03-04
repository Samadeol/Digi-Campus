from django.db import models

# Create your models here.

class messMenu(models.Model) :
    itemName = models.CharField(max_length=25)
    itemPrice = models.IntegerField()