"""chacaoGo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    # Paginas principales
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.main, name='main'),
    #Paginas de sesion
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^login/', views.login, name='login'),
    url(r'^finishlog/', views.finishlog, name='finishlog'),
    #url(r'^adduser/', views.adduser, name='adduser'), vista innecesaria elimnada
    url(r'^redirectuser/', views.redirectuser, name='redirectuser'),
    #Paginas de usuario
    url(r'^userprofile/', views.userprofile, name='userprofile'),
    url(r'^mayorsprofile/', views.mayorsprofile, name='mayorsprofile'),
    url(r'^myevents/', views.myevents, name='myevents'),
    url(r'^mycomments/', views.mycomments, name='mycomments'),
    url(r'^purchases/', views.purchases, name='purchases'),
    url(r'^favorites/', views.favorites, name='favorites'),
    #Paginas de eventos
    url(r'^event/', views.event, name='event'),
    url(r'^addevent/', views.addevent, name='addevent'),
]
