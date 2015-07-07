
from django.shortcuts import render

# Create your views here.
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http      import HttpResponse
from django.template  import Context,loader
from main.forms       import *
from main.models      import * 

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def main(request):
    #t = loader.get_template('main.html')
    #c = Context({'foo': 'bar'})
    logged = 'username' in request.session
    print("Esta loggeado?")
    print(logged)

    dictionary = {'logged':logged }
    if not logged:
        dictionary['form'] = LoginForm()

    return render_to_response('main.html', 
                              dictionary , 
                              context_instance=RequestContext(request)
                              )


def register(request):
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
        return HttpResponse(t.render(c))
    else:
        dictionary = {}
        print("wtf am i doing here?")

    return render_to_response('register.html', dictionary , context_instance=RequestContext(request))
    
    


def adduser(request):
    #Este no deberia llevar vista
    t = loader.get_template('main.html')
    return HttpResponse(t.render({}))

def redirectuser(request):
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
            request.session.modified = True
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

def userprofile(request):
    t = loader.get_template('userprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def mayorsprofile(request):
    t = loader.get_template('mayorsprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def event(request):
    t = loader.get_template('event.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))
