from click import password_option
from django.db import models

# occupation_choice = (
#     ('Student','Student'),
#     ('Staff','Staff'),
#     ('Prof','Proffesor')

# )
# Create your models here.
class Profile(models.Model) :
    username = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    is_student = models.BooleanField()
    is_staff = models.BooleanField()
    is_prof = models.BooleanField()
    #Occupation = models.Choices(occupation_choice)
    def __str__(self):
        return self.username
    
    
