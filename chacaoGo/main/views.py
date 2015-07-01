from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import Context,loader

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))
