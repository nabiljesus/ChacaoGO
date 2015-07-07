
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

    dictionary = {'logged':logged }

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
            t = loader.get_template('main.html')
        else:
            print("No pase la validez D:")
            for field in form:
                print(field.errors)
            dictionary = {'form': UserForm(), 'mensaje': 'Ha ocurrido un error al momento de registro :('}
        #return HttpResponse(t.render(c))
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

        t = '/main'

        username = request.POST['username']
        password = request.POST['password']

        if User.mayLog(username,password):
            userType = User.getType(username)
            request.session['username'] = username
            request.session['type']     = userType
            request.session.modified    = True
        else:
            #Poner mensaje de error from django.contrib import messages
            pass

        #Agregamos la persona a la sesion

    return redirect(t,foo='bar')

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

def mayorsprofile(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    t = loader.get_template('mayorsprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))



#######################
#  Vistas para eventos
#######################

def event(request):
    t = loader.get_template('event.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def addevent(request):
    if not 'username' in request.session:
        return redirect("/main",foo='bar')

    if request.method == 'GET':
        dictionary = {'form': EventForm()}
    elif request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():

            newEvent = Event(
                user        = User.getUser(request.session['username']),
                name        = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                xPosition   = 0.00015484, #form.cleaned_data[''],
                yPosition   = 0.00015484, #form.cleaned_data[''],
                start       = form.cleaned_data['start'],
                end         = form.cleaned_data['end'],
                evenType    = form.cleaned_data['evType']
            )

            newEvent.save()
            c = Context({'mensaje': 'Gracias por agregar eso que agregaste jeje!'})
            t = loader.get_template('main.html') # A donde deberia mandar?
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