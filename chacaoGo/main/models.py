from django.db import models


#######################
# Constantes de Modelos
#######################

TYPECHOICES = (
        ('ZP','Zona Peligrosa'),
        ('DEL','Delito'),
        ('AS','Actividad Sospechosa'),
        ('AC','Accidente'),
        ('EM','Embotellamiento'),
        ('PV','Peligro en la Vía'),
        ('PR','Protesta'),
        ('AM','Asistencia médica'),
        ('SA','Servicio de Agua'),
        ('SE','Servicio Eléctrico'),
        ('RRS','Recolección de Residuos Solidos'),
        ('MA','Maratón'),
        ('ED','Encuentro Deportivo'),
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
        ('SV','Solicitud de Voluntarios'),
        ('CA','Calles y avenidas'),
        ('ACE','Aceras'),
        ('PC','Patrimonio Cultural'),
        ('TE','Terreno')
    )

CATEGORIES = (
    ('SE','Seguridad'),
    ('VI','Vialidad'),
    ('DS','Deficiencia de Servicios'),
    ('DE','Deportes'),
    ('CU','Cultura'),
    ('PR','Productos'),
    ('SP','Servicios Públicos'),
    ('DM','Deterioro Municipal')
)


CATEGORYLIST = ['SE','VI','DS','DE','CU','PR','SP','DM']

def smallerDate(a,b):
    if a.year <= b.year:
        if a.month <= b.year:
            if a.day <= b.year:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

##########
# Modelos
##########

class User(models.Model):
    """Clase para usuario"""
    NORMAL    = 'Usuario'
    MODERATOR = 'Moderador'
    MAYOR     = 'Alcaldía'
    USERTYPES = (
        (NORMAL,   'Usuario'  ),
        (MODERATOR,'Moderador'),
        (MAYOR,    'Alcaldía' )
    )

    username = models.CharField(max_length = 20,primary_key=True)
    fullname = models.CharField(max_length = 30)
    email    = models.EmailField(unique=True)
    password = models.CharField(max_length = 128) #Para sha
    userType = models.CharField(max_length = 9,choices=USERTYPES,default=NORMAL) 
    added    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + self.fullname

    #Funcion que indica si un username con su password concuerdan 
    def mayLog(username,password):
        user = User.objects.filter(username=username)
        if len(user) == 1:
            #Cambiar por clave masfuerte
            return user[0].password == password
        else:
            return False

    #Funcion que entrega un objeto de tipo usuario asociado a un username
    def getUser(username):
        user = User.objects.filter(username=username)
        return user[0]

    #Funcion que entrega el typo del usuario dado
    def getType(username):
        user = User.objects.filter(username=username)
        if len(user) == 1:
            return user[0].userType
        else:
            return None

    def getEvents(username):
        user = User.objects.filter(username=username)
        return Event.objects.filter(user=user[0]).order_by('-added')

class Category(models.Model):
    """Clase para categoria de cada evento""" 
    categoryName = models.CharField(max_length = 2,choices=CATEGORIES)
    eventType    = models.CharField(max_length = 3,choices=TYPECHOICES)

    #Funcion que obtiene todos los tipos asociados a una categoria
    def getTypes(category):
        types = Category.objects.filter(categoryName=category)
        res = []
        for i in types:
            res.append(i.eventType)
        return res

class Event(models.Model):
    """Clase para un evento"""
    DEFAULT     = 'FE'
    
    eventId     = models.AutoField(primary_key=True)
    user        = models.ForeignKey(User)
    name        = models.CharField(max_length = 30)
    description = models.TextField(default = " ")
    xPosition   = models.FloatField()
    yPosition   = models.FloatField()
    added       = models.DateTimeField(auto_now_add=True)
    start       = models.DateTimeField()
    end         = models.DateTimeField()
    evenType    = models.CharField(max_length = 3,choices=TYPECHOICES)
    vip         = models.BooleanField(default = False)
    seen        = models.BooleanField(default = False)

    def getAllComments(id):
        event = Event.objects.filter(eventId=id)[0]
        return Comment.objects.filter(event=event).order_by('-added')

    def getEventById(id):
        return Event.objects.filter(eventId=id)[0]

    def getEventsByType(eventList):
        from django.utils import timezone
        res = {}
        for cat in CATEGORYLIST:
            catEvents   = []
            eventsInCat = Category.getTypes(cat)

            for evType in eventsInCat:
                events = Event.objects.filter(evenType=evType)
                if (len(events) > 0):
                    for e in events:
                        now = timezone.now()

                        #Comparacion unicamente de dias
                        rightInTime = smallerDate(e.start,now)  and \
                                      smallerDate(now,e.end)

                        if not rightInTime:
                            print("Verga primo el ",end="")
                            print(e.name,end="")
                            print(" no furula porque")
                            print(now)
                            print(e.end)

                        if (e.evenType in eventList) and rightInTime:
                            
                            catEvents.append(
                                { 'X'          : e.xPosition ,
                                  'Y'          : e.yPosition,
                                  'nombre'     : e.name,
                                  'descripcion': e.description[0:30] + "...",
                                  'tipo'       : evType,
                                  'id'         : e.eventId,
                                  'VIP'        : e.vip ,
                                }
                            )

            if (len(catEvents) > 0):
                res[cat] = catEvents
        
        return res



class Comment(models.Model):
    """Clase para comentarios asociados a un evento"""
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)
    description = models.CharField(max_length = 500)
    added       = models.DateTimeField(auto_now_add=True)

    def getParentEvent(id):
        return Event.objects.filter(eventId=id)[0]

