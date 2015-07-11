
from django.shortcuts import render

# Create your views here.
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http      import HttpResponse
from django.template  import Context,loader
from main.forms       import *
from main.models      import * 
from django.http import HttpResponseRedirect


#######################
#  Vistas principales
#######################

def index(request):
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def testdrop(request):
    t = loader.get_template('testdrop.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))



def main(request):

    logged = 'username' in request.session
    print("Scrum Nigga master")

    users = ['Alcaldía','Usuario','Moderador']
    listaEventos = Event.getEventsByType(EVENTLIST,users)
    import json
    listaEventos = json.dumps(listaEventos)

    dictionary = {'logged':logged, 'listaEventos': str(listaEventos) }
    return render_to_response('main.html', 
                              dictionary , 
                              context_instance=RequestContext(request)
                              )

def filter(request):
    logged = 'username' in request.session
    print("Scrum Nigga master")

    selectedEvents = EVENTLIST

    if request.method == 'POST':
        if 'fuser' in request.POST:
            if len(request.POST['fuser']) == 2:
                users = ['Alcaldía','Usuario','Moderador']
            else:
                if request.POST['fuser'] == "Usuario":
                    users = ["Usuario"]
                else:
                    users = ['Alcaldía','Moderador']
        else:
            users = ['Alcaldía','Usuario','Moderador']

        if 'type[]' in request.POST:
            selectedEvents = request.POST['type[]']
        else:
            selectedEvents = EVENTLIST

    print(users)

    listaEventos = Event.getEventsByType(selectedEvents,users)
    import json
    listaEventos = json.dumps(listaEventos)

    dictionary = {'logged':logged, 'listaEventos': str(listaEventos) }
    return render_to_response('main.html', 
                              dictionary , 
                              context_instance=RequestContext(request)
                              )
################################
#  Vistas de manejo de usuarios
################################

def register(request):
    dictionary = {}
    if request.method == 'GET':
        dictionary = {'form': UserForm()}
    elif request.method == 'POST':
        form = UserForm(request.POST)
        t = loader.get_template('main.html')
        if form.is_valid():
            newUser = User(
                username = form.cleaned_data['username'],
                fullname = form.cleaned_data['fullname'],
                email    = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                userType = 'Usuario'
            )
            newUser.save()
            c = Context({'mensaje': 'Gracias por registrarte!'})
            return HttpResponseRedirect("/main") #Con esto lo arreglé
            
        else:
            print("No pase la validez D:")
            for field in form:
                print(field.errors)
            dictionary = {'form': UserForm(), 'mensaje': 'Ha ocurrido un error al momento de registro :('}
        return HttpResponse(t.render(c))
    else:
        dictionary = {}
        print("wtf am i doing here?")
    return render_to_response('register.html', dictionary , context_instance=RequestContext(request))

# ELIMINAR CREO
def adduser(request):
    #Este no deberia llevar vista
    t = loader.get_template('main.html')
    return HttpResponse(t.render({}))

def login(request):
    if request.method == 'GET':
        print("No deberias estar aqui, fucker")
        t = '/main'
    elif request.method == 'POST':
        #Verificar que el usuario es correcto

        username = request.POST['username']
        password = request.POST['password']

        if User.mayLog(username,password):
            print("Pase por aqui")
            userType = User.getType(username)
            request.session['username'] = username
            request.session['type']     = userType
            request.session.modified    = True
        else:
            #Poner mensaje de error from django.contrib import messages
            pass
        
    return render_to_response('finishlog.html', {} , context_instance=RequestContext(request))

def finishlog(request):
    t = loader.get_template('finishlog.html')
    return HttpResponse(t.render(c))


def logout(request):
    del request.session['username']
    del request.session['type']
    request.session.modified = True
    return redirect('/main',foo='bar')

#######################
#  Vistas de perfil
#######################

def redirectuser(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')
    
    if   request.session['type'] == 'Usuario':
        html = '/userprofile'
    elif request.session['type'] == 'Alcaldía':
        html = '/mayorsprofile'
    elif request.session['type'] == 'Moderador':
        html = '/mayorsprofile'
    else:
        html = '/main'

    return redirect(html)

def userprofile(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('userprofile.html')
    c = Context({'user': request.session['username']})         
    return HttpResponse(t.render(c))

def checkprofile(request):
    logged = 'username' in request.session

    profile = request.GET.get('username',-1)
    
    if profile == -1:
        return redirect("/main")
    else:


        posts    = User.getCreatedEvents(profile)
        comments = User.getCommentsMade(profile)
        showable = request.session['username'] == profile
        (points,title,image)   = User.getUserVotes(profile)

        dictionary = {
            'posts'   : posts,
            'comments': comments,
            'points'  : points,
            'showable': showable, #Podria permitirse que las autoridades tambien vean este correo
            'email'   : User.getEmail(profile),
            'name'    : User.getName(profile),
            'title'   : title,
            'image'   : image,
        }

        t = loader.get_template('checkprofile.html')

        c = Context(dictionary)         

        return HttpResponse(t.render(c))

def mayorsprofile(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('mayorsprofile.html')
    c = Context({'user': request.session['username']})       
    return HttpResponse(t.render(c))


def myevents(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    userEvents = User.getEvents(request.session['username'])

    t = loader.get_template('myevents.html')
    c = Context({'userEvents': userEvents}) 
    return HttpResponse(t.render(c))

def mycomments(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    userEvents = User.getCommentedEvents(request.session['username'])

    t = loader.get_template('mycomments.html')
    c = Context({'userEvents': userEvents})
    return HttpResponse(t.render(c))

def favorites(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    userEvents = User.getFavoriteEvents(request.session['username'])

    t = loader.get_template('favorites.html')
    c = Context({'userEvents': userEvents})
    return HttpResponse(t.render(c))

def purchases(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    userEvents = User.getPurchases(request.session['username'])

    t = loader.get_template('purchases.html')
    c = Context({'userEvents': userEvents})
    return HttpResponse(t.render(c))

def topusers(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    if (User.getType(request.session['username']) != 'Alcaldía' ) and \
       (User.getType(request.session['username']) != 'Moderador' ):
       return redirect("/main",foo='bar')

    topusers = User.getUsersByPoints()


    t = loader.get_template('topusers.html')
    c = Context({'topusers': topusers}) 
    return HttpResponse(t.render(c))

#######################
#  Vistas para eventos
#######################

def event(request):
    eventId = int(request.GET.get('id',-1))
    logged  = 'username' in request.session

    if eventId != -1:
        event   = Event.getEventById(eventId)
    else:
        event   = Event.getEventById(1)


    comments                      = Event.getAllComments(eventId)
    (positiveVotes,negativeVotes) = Vote.getEventVotes(eventId)
    
    (mayvotep,mayvoten) = Vote.mayVote(request.session['username'],eventId) if \
                         logged else (False,False) 

    reports    = Report.getEventNumberReports(eventId)
    if logged:
        mayReport  = Report.mayReport(eventId,request.session['username'])
        official   = User.getType(request.session['username']) == 'Alcaldía' or\
                     User.getType(request.session['username']) == 'Moderador'
    else:
        mayReport = False
        official  = False


    reportable = Event.reportable(event.evenType)
    print(reportable)

    cred = User.getUserVotes(event.user.username)
    
    image=""
    if event.user.userType == 'Moderador' or event.user.userType == 'Alcaldía':
        ucolor = "#FFCC00"
        image='/static/img/chacao1.jpg'
    elif cred[0] < 0:
        ucolor="#CC0000"
    elif cred[0] < 10:
        ucolor=""
    elif cred[0] < 30:
        ucolor="#E0FFE0"
    else: 
        ucolor="#00FF00"
    categ=Event.getCat(event.evenType)
    print(categ)
    bcolor="#fff";
    timage=""
    if categ=='SE':
        bcolor="#007fff"
        timage="police"
    elif categ=='VI':
        bcolor="#b5b5b5"
        timage="street"
    elif categ=='DS':
        bcolor="#f2cb14"
        timage="servce"
    elif categ=='DE':
        bcolor="#74b54d"
        timage="sports"
    elif categ=='CU':
        bcolor="#7956c0"
        timage="culture"
    elif categ=='PR':
        bcolor="#c06756"
        timage="product"
    elif categ=='SP':
        bcolor="#53d5d3"
        timage="help"
    elif categ=='DM':
        bcolor="#d76adb"
        timage="broken"


    #profile = request.GET.get('username',-1)
    #User.getUserVotes(profile)
    
    dictionary = {
                 'event'   : event,
                 'type'    : event.get_evenType_display(), 
                 'form'    : CommentForm(),
                 'logged'  : logged,
                 'comments': comments,
                 'positives' : positiveVotes,
                 'negatives' : negativeVotes,
                 'mayvotep'  : mayvotep,
                 'mayvoten'  : mayvoten,
                 'reports'   : reports,
                 'mayReport' : mayReport,
                 'reportable': reportable,
                 'official'  : official,
                 'ucolor'    : ucolor,
                 'bcolor'    : bcolor,
                 'image'     : image,
                 'timage'    : timage
                 }


    return render_to_response('event.html', dictionary , context_instance=RequestContext(request))


def addcomment(request):
    
    if request.method == 'GET':
        # print("Que mieeeerda paso aqui")
        pass
    elif request.method == 'POST':

        #Conversion a floats
        eventId = int(request.POST.get('eventId',-1))

        #Convertir post en mutable y elimnar variables de mas
        copy = request.POST.copy()
        copy.pop('eventId')

        form = CommentForm(copy)
        if form.is_valid():

            newComment = Comment(
                user        = User.getUser(request.session['username']),
                description = form.cleaned_data['description'],
                event       = Comment.getParentEvent(eventId)
            )

            newComment.save()
            c = Context({'mensaje': 'Gracias por comentar!'})
            #t = loader.get_template('/event/?id='+str(eventId)) 
            #return render_to_response('/event/?id='+str(eventId), c , context_instance=RequestContext(request))
            return redirect('/event/?id='+str(eventId))
        else:
            print("No pase la validez D:")
            for field in form:
                print(field)
                print(field.errors)
            t = loader.get_template('/event/?id='+str(eventId)) 
            c = Context({'form': CommentForm(), 'mensaje': 'Ha ocurrido un error al momento de crear el evento :('})
        return HttpResponse(t.render(c))
    else:
        dictionary = {}
        print("wtf? what am i doing here?")

    return render_to_response('event.html', dictionary , context_instance=RequestContext(request))


def addevent(request):
    if not 'username' in request.session:
        #Alertar que no esta registrado
        return redirect("/main",foo='bar')

    if request.method == 'GET':
        dictionary = {  
                        'form': EventForm(),
                        'x'   :request.GET.get('x',-1),
                        'y'   :request.GET.get('y',-1)
                     }

    elif request.method == 'POST':

        #Conversion a floats
        x = float(request.POST.get('x',-1))
        y = float(request.POST.get('y',-1))

        #Convertir post en mutable y elimnar variables de mas
        copy = request.POST.copy()
        copy.pop('x')
        copy.pop('y')

        form = EventForm(copy)
        if form.is_valid():

            newEvent = Event(
                user        = User.getUser(request.session['username']),
                name        = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                xPosition   = x, 
                yPosition   = y, 
                start       = form.cleaned_data['start'],
                end         = form.cleaned_data['end'],
                evenType    = form.cleaned_data['evType']
            )

            newEvent.save()
            c = Context({'mensaje': 'Gracias por agregar eso que agregaste jeje!'})
            t = loader.get_template('main.html') # A donde deberia mandar?
            return redirect("/main")
            return render_to_response('main.html', {} , context_instance=RequestContext(request))
        else:
            print("No pase la validez D:")
            for field in form:
                print(field)
                print(field.errors)
            return redirect("/main")
            t = loader.get_template('main.html')
            c = Context({'form': EventForm(), 'mensaje': 'Ha ocurrido un error al momento de crear el evento :('})
        return HttpResponse(t.render(c))
    else:
        dictionary = {}
        print("wtf? what am i doing here?")

    return render_to_response('addevent.html', dictionary , context_instance=RequestContext(request))

def addvote(request):
    print(request.GET)
    vote    = request.GET.get('v',-1)
    eventId = int(request.GET.get('eventId',-1))

    if vote == -1 or not ('username' in request.session):
        return redirect('/event/?id='+str(eventId))
    else:
        user = User.getUser(request.session['username'])
        event= Event.getEventById(eventId)
        vote = vote == "True"
        (mayvotep,mayvoten) = Vote.mayVote(request.session['username'],eventId)

        if mayvotep and mayvoten:
            newVote   = Vote(
                user  = user,
                event = event,
                isUsefull = vote,
            )
            newVote.save()
        else:

            v = Vote.objects.filter(user=user,event=event).first()
            v.isUsefull = vote
            v.save()

        return redirect('/event/?id='+str(eventId))

def addreport(request):
    print(request.GET)
    eventId = int(request.GET.get('eventId',-1))

    if eventId == -1 or not ('username' in request.session):
        return redirect('/event/?id='+str(eventId))
    else:
        user = User.getUser(request.session['username'])
        event= Event.getEventById(eventId)
        

        if Report.mayReport(eventId,request.session['username']):
            newReport = Report(
                user  = user,
                event = event
            )
            newReport.save()
        else:
            pass

        return redirect('/event/?id='+str(eventId))

def mostreported(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    print(User.getType(request.session['username']))
    
    if (User.getType(request.session['username']) != 'Alcaldía' ) and \
       (User.getType(request.session['username']) != 'Moderador' ):
       return redirect("/main",foo='bar')

    reports = Report.getReports()

    t = loader.get_template('mostreported.html')
    c = Context({'reports': reports}) 
    return HttpResponse(t.render(c))

def seen(request):
    eventId = int(request.GET.get('eventId',-1))

    if eventId == -1 or not ('username' in request.session):
        return redirect('/event/?id='+str(eventId))
    else:
        
        if (User.getType(request.session['username']) != 'Alcaldía' ) and \
           (User.getType(request.session['username']) != 'Moderador' ):
            return redirect("/main",foo='bar')

        event= Event.getEventById(eventId)
        event.seen = True
        event.save()

        return redirect('/mostreported/')
