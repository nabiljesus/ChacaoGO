from django.db import models

# Create your models here.
class User(models.Model):
    """Clase para usuario"""
    username = models.CharField(max_length = 20,primary_key=True)
    fullname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 128) #Para sha
    userType = models.CharField(max_length = 11) 
    added    = models.DateTimeField(auto_now_add=True) 

class Event(models.Model):
    """Clase para un evento"""
    user        = models.ForeignKey(User)
    name        = models.CharField(max_length = 30)
    description = models.CharField(max_length = 500)
    xPosition   = models.FloatField()
    yPosition   = models.FloatField()
    added       = models.DateTimeField(auto_now_add=True)
    start       = models.DateTimeField()
    end         = models.DateTimeField()


class Comment(models.Model):
    """Clase para comentarios asociados a un evento"""
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)
    description = models.CharField(max_length = 500)
    added       = models.DateTimeField(auto_now_add=True)
