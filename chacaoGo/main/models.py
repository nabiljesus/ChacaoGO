from django.db import models

TYPECHOICES = (
        ('ZP','Zona Peligrosa'),
        ('DEL','Delito'),
        ('AS','Actividad Sospechosa'),
        ('AC','Accidente'),
        ('EM','Embotellamiento'),
        ('PV','Peligro en la Vía'),
        ('PR','Protesta'),
        ('AM','Asistencia médica'),
        ('RSE','Reparacion Servicio Electrico'),
        ('RRS','Recolección de Residuos Solidos'),
        ('MA','Maratón'),
        ('BA','Bailoterapia'),
        ('YO','Yoga'),
        ('CD','Clase Deportiva'),
        ('CO','Concierto'),
        ('FE','Feria'),
        ('OT','Obra de Teatro'),
        ('EA','Exposición de arte'),
        ('JD','Jornada de Documentación'),
        ('VPE','Venta de Producto Escaso'),
        ('JE','Jornada Electoral'),
        ('DES','Descuento'),
        ('DS','Donación de sangre'),
        ('SM','Solicitud de Medicamento'),
        ('JV','Jornada Veterinaria'),
        ('SV','Solicitud de Voluntarios')
    )       

# Create your models here.
class User(models.Model):
    """Clase para usuario"""
    NORMAL    = 'Usuario'
    MODERATOR = 'Moderador'
    MAYOR     = 'Alcaldía'
    TYPECHOICES = (
        (NORMAL,   'Usuario'  ),
        (MODERATOR,'Moderador'),
        (MAYOR,    'Alcaldía' )
    )

    username = models.CharField(max_length = 20,primary_key=True)
    fullname = models.CharField(max_length = 30)
    email    = models.EmailField(unique=True)
    password = models.CharField(max_length = 128) #Para sha
    userType = models.CharField(max_length = 9,choices=TYPECHOICES,default=NORMAL) 
    added    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + self.fullname

    def mayLog(username,password):
        user = User.objects.filter(username=username)
        if len(user) == 1:
            #Cambiar por clave masfuerte
            return user[0].password == password
        else:
            return False

    def getType(username):
        user = User.objects.filter(username=username)
        if len(user) == 1:
            return user[0].userType
        else:
            return None
        

class Event(models.Model):
    """Clase para un evento"""
    DEFAULT     = 'FE'
    

    eventId     = models.AutoField(primary_key=True)
    user        = models.ForeignKey(User)
    name        = models.CharField(max_length = 30)
    description = models.CharField(max_length = 500)
    xPosition   = models.FloatField()
    yPosition   = models.FloatField()
    added       = models.DateTimeField(auto_now_add=True)
    start       = models.DateTimeField()
    end         = models.DateTimeField()
    evType      = models.CharField(max_length = 3,choices=TYPECHOICES,default=DEFAULT)
    vip         = models.BooleanField(default = False)
    seen        = models.BooleanField(default = False)

class Comment(models.Model):
    """Clase para comentarios asociados a un evento"""
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)
    description = models.CharField(max_length = 500)
    added       = models.DateTimeField(auto_now_add=True)
