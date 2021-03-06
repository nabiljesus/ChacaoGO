from django.db import models
from django.db.models import Count


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
        ('EDU','Educación'),
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

CATEGORYIMAGE = {
    'DM' : "icon_broken.png",
    'CU' : "icon_culture.png",
    'SP' : "icon_help.png",
    'SE' : "icon_police.png",
    'PR' : "icon_product.png",
    'DS' : "icon_service.png",
    'DE' : "icon_sports.png",
    'VI' : "icon_street.png"
}

CATEGORYLIST         = ['SE','VI','DS','DE','CU','PR','SP','DM']
REPORTABLECATEGORIES = ['SE','VI','DS','SP','DM']
EVENTLIST    = ['ZP','DEL','AS','AC','EM','PV','PR','AM','SA','SE','RRS','MA','ED','BA','YO','CD','CO','FE','OT','EA','JD','VPE','JE','DES','DS','SM','JV','SV','CA','AC','PC','TE']

LEVELS  = [ ("Pinocho",                       0   , 'cred_pinocho.png'),
            ("Ciudadano común",               0   , 'cred_common.png'),
            ("Buen samaritano",               10  , 'cred_good.png'),
            ("Viejita de la comunidad",       30  , 'cred_granny.png'),
            ("Ciudadano Ejemplar",            40  , 'cred_exemplar.png'),
            ("Periodista aficionado",         60  , 'cred_journalistwannabe.png'),
            ("Ciberperiodista",               70  , 'cred_ciberjournalist.png'),
            ("Colaborador conocido ChacaoGO", 100 , 'cred_chacaoGO1.png'),
            ("Colaborador Destacado Chacao",  150 , 'cred_chacaoGO2.png'),
            ("Mano dereha de Ramón Muchacho", 300 , 'cred_chacaoGO3.png')
           ]


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

def deletRepeated(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

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
        user = User.objects.filter(username=username).first()
        return Event.objects.filter(user=user).order_by('-added')

    def getPurchases(username):
        user = User.objects.filter(username=username).first()
        return Event.objects.filter(user=user,vip=True).order_by('-added')


    def getCommentedEvents(username):
        user     = User.objects.filter(username=username)
        
        eventsCommented = Comment.objects.filter(user=user)\
                            .order_by('-added')

        #Asegurando la unicidad
        a = set()
        for comment in eventsCommented:
            event = comment.event
            a.add( (event.name,event.description,event.eventId))

        return a

    def getFavoriteEvents(username):
        user     = User.objects.filter(username=username)
        
        eventsLiked = Vote.objects.filter(user=user,isUsefull=True)

        #Asegurando la unicidad
        a = set()
        for vote in eventsLiked:
            event = vote.event
            a.add( (event.name,event.description,event.eventId))

        return a

    def getCreatedEvents(username):
        user = User.objects.filter(username=username).first()
        return Event.objects.filter(user=user).count()

    #Funcion para obtener el balance de votos de un usuario segun sus eventos
    #Ademas entrega el titulo correspondiente 
    def getUserVotes(username):
        user    = User.objects.filter(username=username)[0]
        events  = Event.objects.filter(user=user)
        voteSum = 0

        for ev in events:
            votes = Vote.objects.filter(event=ev)
            positive = votes.filter(isUsefull=True).count()
            negative = votes.filter(isUsefull=False).count()
            voteSum  = voteSum + positive - negative

        for l in LEVELS:
            if voteSum < 0:
                title = LEVELS[0][0]
                image = LEVELS[0][2]
                pass
            elif voteSum >= l[1]:
                title = l[0]
                image = l[2]
                pass
            else:
                break
            

        return (voteSum,title,image)

    def getUsersByPoints():
        from django.db.models import Q

        #Ciudadanos
        usuarios = User.objects.filter(~Q(userType='Alcaldía') & 
                                       ~Q(userType='Moderador'))

        #Usuarios y sus votos positivos
        positives = Vote.objects.filter(isUsefull=True).\
                             values('event').\
                                values('event__user').\
                                    annotate(positive=Count('event'))

        #Usuarios y sus votos negativos
        negatives = Vote.objects.filter(isUsefull=False).\
                             values('event').\
                                values('event__user').\
                                    annotate(negative=Count('event'))
        res = []
        count = 0
        for u in usuarios:
            res.append({ 'user': u, 'points': 0})
            for p in positives:
                if u.username == p['event__user']:
                    res[count]['points'] = p['positive']
            for p in negatives:
                if u.username == p['event__user']:
                    res[count]['points'] = res[count]['points'] - p['negative']
            count += 1


        #return sorted(res,key=lambda x: x[1]['points'],reverse=True)
        from operator import itemgetter
        return sorted(res, key=itemgetter('points'),reverse=True)

        #from main.models import *
        #User.getUsersByPoints()

    def getCommentsMade(username):
        user = User.objects.filter(username=username).first()
        return Comment.objects.filter(user=user).count()

    def getEmail(username):
        user = User.objects.filter(username=username).first()
        return user.email

    def getName(username):
        user = User.objects.filter(username=username).first()
        return user.fullname



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

    def getEventsByType(eventList,users):
        from django.utils import timezone
        res = {}
        for cat in CATEGORYLIST:
            catEvents   = []
            eventsInCat = Category.getTypes(cat)

            for evType in eventsInCat:
                if len(users) == 3:
                    #Consulta normal, agarro todos
                    events = Event.objects.filter(evenType=evType)
                if len(users) == 2:
                    #Consulta con los dos oficiales
                    events = (Event.objects.filter(user__userType='Moderador') | Event.objects.filter(user__userType='Alcaldía')).filter(evenType=evType)
                if len(users) == 1:
                    #Consulta de solo ciudadano
                    events = (Event.objects.filter(user__userType='Usuario')).filter(evenType=evType)
                    

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


    def getCat(etype):
        return Category.objects.filter(eventType=etype)[0].categoryName

    def reportable(eventType):
        return Category.objects.filter(eventType=eventType).first().categoryName in REPORTABLECATEGORIES



class Comment(models.Model):
    """Clase para comentarios asociados a un evento"""
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)
    description = models.CharField(max_length = 500)
    added       = models.DateTimeField(auto_now_add=True)

    def getParentEvent(id):
        return Event.objects.filter(eventId=id)[0]

class Vote(models.Model):
    """Clase para votos de utilidad en un evento"""
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)
    isUsefull   = models.BooleanField()

    class Meta:
        unique_together = ('user','event')

    #Funcion para obtener numero de votos positivos y negativos de un evento
    def getEventVotes(eventId):
        event = Event.objects.filter(eventId=eventId)[0]
        votes = Vote.objects.filter(event=event)

        positive = votes.filter(isUsefull=True).count()
        negative = votes.filter(isUsefull=False).count()

        return (positive,negative)

    #Funcion que indica por que puede votar un usuario en un evento
    def mayVote(username,eventId):
        user    = User.objects.filter(username=username).first()
        event   = Event.objects.filter(eventId=eventId).first()

        vote    = Vote.objects.filter(event=event,user=user)

        if(vote.count() == 0 ):
            return (True, True)
        else:
            if vote.first().isUsefull:
                return (False,True)
            else:
                return (True,False)


class Report(models.Model):
    """Clase para votos de utilidad en un evento"""
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)


    class Meta:
        unique_together = ('user','event')

    #Funcion para obtener numero de votos positivos y negativos de un evento
    def getReports():
        return Event.objects.filter(seen=False).annotate(repCount=Count('report')).order_by('-repCount')

    def getEventNumberReports(eventId):
        event=Event.objects.filter(eventId=eventId)
        return Report.objects.filter(event=event).count()

    def mayReport(eventId,username):
        event = Event.objects.filter(eventId=eventId)
        user  = User.objects.filter(username=username)

        return Report.objects.filter(user=user,event=event).count() == 0
