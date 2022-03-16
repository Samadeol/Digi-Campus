from click import password_option
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Profile(models.Model) :
    # logged_in = models.BooleanField(default=False)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    room_no = models.CharField(max_length=4)
    hall_no = models.IntegerField()
    roll_no = models.IntegerField()
    mobile_no=models.IntegerField()
    is_student = models.BooleanField()
    is_staff = models.BooleanField()
    is_prof = models.BooleanField()
    def __str__(self):
        return self.username