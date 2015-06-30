from django.db import models

# Create your models here.
class User(models.Model):
    """Clase para usuario"""
    username = models.CharField(max_length = 20,primary_key=True)
    fullname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 128) #Para sha512
    userType = models.CharField(max_length = 11)  # 


