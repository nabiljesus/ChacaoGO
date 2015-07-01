from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import Context,loader

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
    t = loader.get_template('register.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))



def adduser(request):
    #Este no deberia llevar vista
    t = loader.get_template('main.html')
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


