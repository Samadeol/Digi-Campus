from click import password_option
from django.db import models

# Create your models here.
class database(models.Model) :
    username = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    
    
