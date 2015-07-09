
from django.shortcuts import render

# Create your views here.
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http      import HttpResponse
from django.template  import Context,loader
from main.forms       import *
from main.models      import * 

def kickout(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

#######################
#  Vistas principales
#######################

def index(request):
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def main(request):

    logged = 'username' in request.session

    listaEventos = Event.getEventsByType(['ZP','DEL','AS','AC','EM','PV','PR','AM','SA','SE','RRS','MA','ED','BA','YO','CD','CO','FE','OT','EA','JD','VPE','JE','DES','DS','SM','JV','SV','CA','AC','PC','TE'])
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
        html = '/userprofile'
    else:
        html = '/main'

    return redirect(html)

def userprofile(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('userprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def checkprofile(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('checkprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def mayorsprofile(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('mayorsprofile.html')
    c = Context({'foo': 'bar'})         
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

    t = loader.get_template('mycomments.html')
    return HttpResponse(t.render({}))

def favorites(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('favorites.html')
    return HttpResponse(t.render({}))

def purchases(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('purchases.html')
    return HttpResponse(t.render({}))

#######################
#  Vistas para eventos
#######################

def event(request):
    eventId = int(request.GET.get('id',-1))

    if eventId != -1:
        event   = Event.getEventById(eventId)
    else:
        event   = Event.getEventById(1)

    comments = Event.getAllComments(eventId)
    print(comments)
    
    dictionary = {
                 'event'   : event,
                 'type'    : event.get_evenType_display(), 
                 'form'    : CommentForm(),
                 'logged'  : 'username' in request.session,
                 'comments': comments
                 }


    return render_to_response('event.html', dictionary , context_instance=RequestContext(request))


def addcomment(request):
    print("TE JURO QUE PASE POR AQUI")
    if request.method == 'GET':
        print("Que mieeeerda paso aqui")
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

    return render_to_response('addevent.html', dictionary , context_instance=RequestContext(request))


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
            return render_to_response('main.html', {} , context_instance=RequestContext(request))
            return redirect("/main")
        else:
            print("No pase la validez D:")
            for field in form:
                print(field)
                print(field.errors)
            t = loader.get_template('main.html')
            c = Context({'form': EventForm(), 'mensaje': 'Ha ocurrido un error al momento de crear el evento :('})
        return HttpResponse(t.render(c))
    else:
        dictionary = {}
        print("wtf? what am i doing here?")

    return render_to_response('addevent.html', dictionary , context_instance=RequestContext(request))