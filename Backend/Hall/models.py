from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HallStudents(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

class hallPresence(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_visiting=models.ForeignKey(HallStudents, on_delete=models.CASCADE)
    in_hall=False
    timeEntered=models.DateTimeField()
    timeExit=models.DateTimeField()
    
