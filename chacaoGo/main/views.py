from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import Context,loader
from main.forms       import UserForm

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def main(request):
    t = loader.get_template('main.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def register(request):
    form = UserForm()
    t = loader.get_template('register.html')
    c = Context({'form': form})         
    return HttpResponse(t.render(c))



def adduser(request):
    #Este no deberia llevar vista
    t = loader.get_template('adduser.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def userprofile(request):
    t = loader.get_template('userprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def mayorsprofile(request):
    t = loader.get_template('mayorsprofile.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def mayorsprofile(request):
    t = loader.get_template('event.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))


